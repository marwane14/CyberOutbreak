# run_sim.py
import os, sys, time, json, math, random, tempfile, argparse
from typing import Dict

try:
    import yaml  # pip install pyyaml
except Exception:
    yaml = None

# ---------------- Paths ----------------
ROOT = os.path.dirname(__file__)
UI_STATIC = os.path.join(ROOT, "ui", "static")
STATUS = os.path.join(UI_STATIC, "status.json")
METRICS = os.path.join(UI_STATIC, "metrics.csv")
os.makedirs(UI_STATIC, exist_ok=True)

# -------------- IO helpers -------------
def _atomic_write(path: str, data: str):
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path), prefix=".tmp_", suffix=".json")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(data)
        f.write("\n")
    os.replace(tmp, path)

def save_status(obj: Dict):
    _atomic_write(STATUS, json.dumps(obj, ensure_ascii=False))

def append_metrics(state: Dict):
    header = "time,infected,total,percent_infected,experts,researching\n"
    if not os.path.exists(METRICS):
        with open(METRICS, "w", encoding="utf-8", newline="") as f:
            f.write(header)
    row = f"{state['time']},{state['metrics']['infected']},{state['metrics']['total']},{state['metrics']['percent_infected']},{state['metrics']['experts']},{state['metrics']['researching']}\n"
    with open(METRICS, "a", encoding="utf-8", newline="") as f:
        f.write(row)

# -------------- Config ------------------
def make_default_cfg():
    return {
        "hosts": 32,
        "routers": 8,
        "tick_seconds": 1.0,
        "dt": 2.0,  # incrément de temps simulé par tick
        "attackers": [1, 12],
        "virus": {"name": "slowPersistent", "desc": "Slow and persistent. Hard to eradicate."},
        "research_threshold": 200.0,
        "seed": 42,
    }

def load_cfg(path: str | None):
    cfg = make_default_cfg()
    if path and os.path.exists(path) and yaml:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if isinstance(data, dict):
            cfg.update(data)
    return cfg

def normalize_cfg(cfg: Dict):
    v = cfg.get("virus")
    if isinstance(v, str) or v is None:
        cfg["virus"] = {"name": v or "unknown", "desc": cfg.get("virus_desc", "")}
    elif isinstance(v, dict):
        cfg["virus"].setdefault("name", "unknown")
        cfg["virus"].setdefault("desc", "")
    # types forts
    for k in ("hosts", "routers"):
        cfg[k] = int(str(cfg.get(k, 0)).strip() or 0)
    for k in ("tick_seconds", "dt"):
        cfg[k] = float(str(cfg.get(k, 1)).strip() or 1)
    # attackers tolérant
    atk = cfg.get("attackers", [])
    if isinstance(atk, str):
        parts = [p.strip() for p in atk.replace(";", ",").replace(" ", ",").split(",") if p.strip()]
        cfg["attackers"] = [int(x) for x in parts if x.isdigit()]
    elif isinstance(atk, list):
        cfg["attackers"] = [int(x) for x in atk if str(x).isdigit()]
    else:
        cfg["attackers"] = []
    return cfg

# -------------- Model -------------------
PROFILES = ["novice", "expert", "absent"]

def build_initial_state(cfg: Dict):
    random.seed(cfg["seed"])
    n = int(cfg["hosts"])
    rcount = int(cfg["routers"])

    hosts = []
    for i in range(n):
        profile = random.choices(PROFILES, weights=[6, 2, 2])[0]
        vpn = random.random() < 0.35
        infected = True  # 100% infecté au départ (comme tes exemples)
        researching = (profile == "expert") and infected and (random.random() < 0.7)
        latency = 0.25 if vpn else 0.0
        hosts.append({
            "id": i,
            "profile": profile,
            "vpn": vpn,
            "infected": infected,
            "time_infected": float(random.choice([2,4,6,8,10,12,14,18,20,22,28,32,34])),
            "latency": latency,
            "router": i % rcount,
            "researching": researching,
            "friends": [],  # rempli après
            "attacker": False
        })

    # attackers
    for a in cfg.get("attackers", []):
        if 0 <= a < n:
            hosts[a]["attacker"] = True
            hosts[a]["time_infected"] = 0.0

    # graphe d'amis simple: anneau + chord
    for i in range(n):
        nb = [(i-1) % n, (i+1) % n, (i+rcount) % n]
        hosts[i]["friends"] = sorted(set(nb))

    # routers meta
    rtypes = {}
    for r in range(rcount):
        if r % 6 == 0:
            t = "protected"
        elif r % 6 == 5:
            t = "intelligent"
        else:
            t = "public"
        rtypes[str(r)] = t

    state = {
        "schema_version": 1,
        "sim_id": "default",
        "time": 0.0,
        "hour": 12,
        "day": 1,
        "virus": cfg["virus"],
        "hosts": hosts,
        "metrics": {"total": n, "infected": n, "percent_infected": 1.0, "experts": 0, "researching": 0},
        "research": {"progress": 0.0, "threshold": float(cfg["research_threshold"])},
        "routers": {"count": rcount, "types": rtypes},
        # "router_edges": [[i, (i+rcount) % n] for i in range(n)],  # optionnel
    }
    compute_metrics(state)
    return state

def compute_metrics(state: Dict):
    hosts = state["hosts"]
    n = len(hosts)
    infected = sum(1 for h in hosts if h["infected"])
    experts = sum(1 for h in hosts if h["profile"] == "expert")
    researching = sum(1 for h in hosts if h.get("researching"))
    state["metrics"] = {
        "total": n,
        "infected": infected,
        "percent_infected": infected / n if n else 0.0,
        "experts": experts,
        "researching": researching,
    }

def step(state: Dict, dt: float):
    # temps
    total_hours = state["hour"] + int(dt)
    state["day"] += total_hours // 24
    state["hour"] = total_hours % 24
    state["time"] = round(state["time"] + dt, 1)

    # recherche
    researching = state["metrics"]["researching"]
    state["research"]["progress"] = round(state["research"]["progress"] + 2.0 + 0.3 * researching, 6)

    # toggles aléatoires sur experts infectés
    for h in state["hosts"]:
        if h["profile"] == "expert" and h["infected"] and random.random() < 0.05:
            h["researching"] = not h["researching"]

    # guérisons lentes si progression suffisante
    thr = state["research"]["threshold"]
    prog = state["research"]["progress"]
    if prog > 0.25 * thr:
        cure_rate = 0.01
        to_cure = max(1, int(state["metrics"]["infected"] * cure_rate))
        candidates = [h for h in state["hosts"] if h["infected"] and not h.get("attacker")]
        random.shuffle(candidates)
        for h in candidates[:to_cure]:
            h["infected"] = False
            h["researching"] = False

    # temps d'infection
    for h in state["hosts"]:
        if h["infected"]:
            h["time_infected"] = round(h["time_infected"] + dt, 1)

    compute_metrics(state)

# -------------- Main --------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()

    cfg = normalize_cfg(load_cfg(args.config))
    if args.seed is not None:
        cfg["seed"] = args.seed

    state = build_initial_state(cfg)

    print(f"Simulator started: hosts={cfg['hosts']} routers={cfg['routers']} virus={cfg['virus']['name']}")
    try:
        tick_seconds = float(cfg["tick_seconds"])
        dt = float(cfg["dt"])
        while True:
            save_status(state)
            append_metrics(state)
            time.sleep(tick_seconds)
            step(state, dt)
    except KeyboardInterrupt:
        print("Stopped")

if __name__ == "__main__":
    main()
