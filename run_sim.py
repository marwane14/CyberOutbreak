# simulator/run_sim.py - routers, router-types, human contacts, experts-only research, day/night
import json, time, random, threading, os
from dataclasses import dataclass, asdict

OUT = os.path.join(os.path.dirname(__file__), '..', 'ui', 'static', 'status.json')

@dataclass
class Virus:
    name: str
    base_prob: float
    persistence: float
    description: str = ""

@dataclass
class Host:
    id:int
    profile:str    # 'expert' or 'novice' or 'absent'
    vpn:bool
    infected:bool=False
    time_infected:float=None
    latency:float=0.0
    router:int=0
    researching:bool=False
    friends:list=None

    def to_dict(self):
        return asdict(self)

class Simulator:
    def __init__(self, n=32, seed=None, virus=None, routers=8, vpn_rate=0.25):
        if seed is not None:
            random.seed(seed)
        # viruses
        self.viruses = {
            'slowworm': Virus('slowworm', base_prob=0.20, persistence=1.5, description='Slow but persistent.'),
            'fastbug':  Virus('fastbug',  base_prob=0.45, persistence=0.8, description='Fast spreading, easier to cure.'),
        }
        self.virus = self.viruses.get(virus, self.viruses['slowworm'])
        self.hosts = []
        self.routers = max(1, routers)
        # router types distribution
        types = ['public','protected','intelligent']
        self.router_types = {r: random.choices(types, weights=[0.4,0.4,0.2])[0] for r in range(self.routers)}
        self.router_type_mult = {'public':1.0, 'protected':0.6, 'intelligent':0.2}
        # create hosts (round-robin routers to get ~equal per router)
        for i in range(n):
            profile = random.choices(['expert','novice','absent'], weights=[0.18,0.62,0.20])[0]
            vpn = random.random() < vpn_rate
            latency = 0.25 if vpn else 0.0
            router = i % self.routers
            self.hosts.append(Host(i, profile, vpn, False, None, latency, router, False, []))
        # friends groups across routers (1-4 friends each)
        ids = [h.id for h in self.hosts]
        for h in self.hosts:
            friends = set()
            num = random.randint(1,4)
            while len(friends) < num:
                f = random.choice(ids)
                if f != h.id:
                    friends.add(f)
            h.friends = sorted(list(friends))
        # patient zero cannot be expert
        candidates = [h for h in self.hosts if h.profile != 'expert']
        p0 = random.choice(candidates)
        p0.infected = True
        p0.time_infected = 0.0
        # time & day/night
        self.t = 0.0
        self.hour = 0
        self.day = 0
        self.lock = threading.Lock()
        # research only by experts
        self.research_progress = 0.0
        self.research_base = {'expert': 0.6, 'novice': 0.0, 'absent': 0.0}
        self.research_speed = {'expert': 1.0, 'novice': 0.0, 'absent': 0.0}
        self.router_intra_mult = 1.0
        self.router_inter_mult = 0.35
        self.contact_prob = 0.03
        self.cure_threshold = 100.0

    def step(self, dt=1.0):
        with self.lock:
            newly = []
            # network propagation
            for h in self.hosts:
                if h.infected:
                    for target in self.hosts:
                        if target.infected:
                            continue
                        p = self.virus.base_prob
                        if target.router == h.router:
                            p *= self.router_intra_mult
                        else:
                            p *= self.router_inter_mult
                        rtype = self.router_types.get(target.router, 'public')
                        p *= self.router_type_mult.get(rtype, 1.0)
                        if target.profile == 'expert':
                            p *= 0.25
                        if target.profile == 'novice':
                            p *= 1.0
                        if target.profile == 'absent':
                            p *= 0.6
                        if target.vpn:
                            p *= 0.35
                        if random.random() < p * (1 - target.latency):
                            newly.append(target)
            # human contact propagation (friends)
            for h in self.hosts:
                if h.infected:
                    for fid in h.friends:
                        target = self.hosts[fid]
                        if target.infected:
                            continue
                        if random.random() < self.contact_prob:
                            newly.append(target)
            # apply infections and possible research start (experts only)
            for t in newly:
                t.infected = True
                t.time_infected = self.t + dt
                if t.profile == 'expert' and random.random() < self.research_base.get('expert',0.0):
                    t.researching = True
            # experts may proactively start researching (daytime more likely)
            for h in self.hosts:
                if h.profile == 'expert' and not h.researching and not h.infected:
                    detect_chance = 0.01 if (6 <= self.hour <= 20) else 0.002
                    if random.random() < detect_chance:
                        h.researching = True
            # research accrual (experts only)
            research_gain = 0.0
            for h in self.hosts:
                if h.researching and h.profile == 'expert':
                    speed = self.research_speed.get(h.profile, 0.0)
                    research_gain += speed * (1.0 / self.virus.persistence) * dt
            self.research_progress += research_gain
            if self.research_progress >= self.cure_threshold:
                for h in self.hosts:
                    h.infected = False
                    h.time_infected = None
                    h.researching = False
                self.research_progress = 0.0
            # advance time (dt in hours)
            self.t += dt
            self.hour = int(self.t) % 24
            self.day = int(self.t) // 24
            self.dump_status()

    def dump_status(self):
        data = {
            'time': self.t,
            'hour': self.hour,
            'day': self.day,
            'virus': {'name': self.virus.name, 'desc': self.virus.description},
            'hosts':[h.to_dict() for h in self.hosts],
            'metrics': self.metrics(),
            'research': {'progress': self.research_progress, 'threshold': self.cure_threshold},
            'routers': {'count': self.routers, 'types': self.router_types}
        }
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        with open(OUT, 'w') as f:
            json.dump(data, f, indent=2)

    def metrics(self):
        total = len(self.hosts)
        infected = sum(1 for h in self.hosts if h.infected)
        experts = sum(1 for h in self.hosts if h.profile=='expert')
        researching = sum(1 for h in self.hosts if h.researching)
        return {'total': total, 'infected': infected, 'percent_infected': infected/total, 'experts': experts, 'researching': researching}

    def run(self, interval=1.0, max_time=None):
        self.dump_status()
        while True:
            if max_time is not None and self.t >= max_time:
                break
            time.sleep(interval)
            self.step(interval)

if __name__ == '__main__':
    sim = Simulator(n=32, seed=42, virus='slowworm', routers=8, vpn_rate=0.25)
    print('Starting simulator with', len(sim.hosts), 'hosts across', sim.routers, 'routers. Status ->', OUT)
    sim.run()