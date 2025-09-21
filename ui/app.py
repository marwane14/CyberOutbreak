# ui/app.py - minimal Flask UI polling status.json
from flask import Flask, jsonify, render_template, send_from_directory
import os, json
app = Flask(__name__, template_folder='templates', static_folder='static')

STATUS = os.path.join(os.path.dirname(__file__), 'static', 'status.json')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    if not os.path.exists(STATUS):
        return jsonify({'error':'no status yet'}), 404
    with open(STATUS, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
