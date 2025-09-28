# en haut
from flask import Flask, jsonify, render_template, Response, send_file, request, stream_with_context
import os, json, time

HERE = os.path.dirname(__file__)
TEMPLATES = os.path.join(HERE, "templates")
STATIC = os.path.join(HERE, "static")
STATUS = os.path.join(STATIC, "status.json")
METRICS = os.path.join(STATIC, "metrics.csv")
RESET_REQ = os.path.join(STATIC, "reset.json")

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route("/")
def index():
    return render_template("index_sse.html")

@app.route("/status")
def status():
    if not os.path.exists(STATUS):
        return jsonify({"error": "no status yet"}), 404
    with open(STATUS, "r", encoding="utf-8") as f:
        return jsonify(json.load(f))

@app.route("/events")
def events():
    def stream():
        last_mtime = None
        while True:
            try:
                mtime = os.path.getmtime(STATUS)
                if mtime != last_mtime:
                    last_mtime = mtime
                    with open(STATUS, "r", encoding="utf-8") as f:
                        data = f.read().strip()
                    yield f"data: {data}\n\n"
                else:
                    yield ": keep-alive\n\n"
            except FileNotFoundError:
                yield ": waiting\n\n"
            time.sleep(1.0)

    resp = Response(stream_with_context(stream()), mimetype="text/event-stream")
    resp.headers["Cache-Control"] = "no-cache"
    resp.headers["Connection"] = "keep-alive"
    resp.headers["X-Accel-Buffering"] = "no"
    return resp

@app.route("/metrics.csv")
def metrics_csv():
    if not os.path.exists(METRICS):
        return ("", 204)
    r = send_file(METRICS, mimetype="text/csv", as_attachment=True, download_name="metrics.csv")
    r.headers["Cache-Control"] = "no-cache"
    return r

@app.route("/reset", methods=["POST"])
def reset():
    os.makedirs(STATIC, exist_ok=True)
    payload = request.get_json(silent=True) or {}
    with open(RESET_REQ, "w", encoding="utf-8") as f:
        json.dump(payload, f)
    return jsonify({"ok": True, "received": payload})

if __name__ == "__main__":
    # important: pas de reloader qui ouvre 2 process
    app.run(debug=True, use_reloader=False)
