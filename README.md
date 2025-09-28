## CyberOutbreak 🦠💻

CyberOutbreak est un laboratoire pédagogique interactif qui simule la propagation d’une infection dans un réseau informatique.
Il permet de visualiser en temps réel comment un virus se propage et comment la défense (humaine ou automatisée) peut ralentir ou stopper l’attaque.

L’objectif : transformer des concepts abstraits de cybersécurité en scénarios concrets et observables.
---

## 🎯 Objectifs

- Illustrer les analogies entre virus biologiques et infections numériques.
- Montrer l’importance de la segmentation réseau et des mécanismes de défense.
- Comparer les comportements de différents profils d’utilisateurs (expert, novice, absent) face à une attaque.
- Mesurer l’impact de la recherche et des contre-mesures dans la réduction d’une infection.
- Fournir un outil simple et visuel pour sensibiliser et apprendre la cybersécurité.

---

## ⚙️ Fonctionnalités actuelles

- Simulation réseau avec hôtes ayant des profils variés (expert, novice, absent).
- Propagation configurable : vitesse, probabilité, rôle des attaquants, présence d’un VPN.
- Backend Flask diffusant l’état du réseau en temps réel via Server-Sent Events (SSE).
- Interface web interactive :
  - Graphe dynamique avec Cytoscape.js (noeuds = machines, liens = connexions).
  - Courbes d’évolution avec Chart.js (% d’infectés dans le temps).
  - Tableaux de bord simples (KPI, progression de la recherche).
- Indicateurs en direct : nombre total d’hôtes, nombre infectés, pourcentage d’infection, progression de la recherche.
- Exports JSON et CSV pour conserver l’historique et analyser les résultats.
- Scénarios personnalisables via fichiers YAML (taille du réseau, nombre d’attaquants, type de virus).

---
## 🔧 Améliorations en cours

Le projet est encore en construction.
Les prochaines étapes :

- Simplifier l’utilisation (lancer un scénario en un clic, documentation claire).
- Optimiser les performances pour simuler des réseaux plus grands.
- Rendre les scénarios plus riches en informations et en visualisation.
- Corriger les bugs connus, notamment deux machines qui restent infectées en permanence.
- Ajouter des fonctionnalités : mode “replay” de la simulation, nouvelles métriques, segmentation avancée.

## 🚀 Installation et exécution

### 1. Cloner le projet
```bash
git clone https://github.com/marwane14/CyberOutbreak.git
cd CyberOutbreak
```

Installation et exécution (local, sans Docker)
---------------------------------------------
```bash
pip install -r requirements.txt

# Dans un terminal : lancer la simulation
python simulator/run_sim.py

# Dans un autre terminal : lancer l'UI
python ui/app.py

# Ouvrir http://127.0.0.1:5000
```

👉 CyberOutbreak est pensé comme un bac à sable pédagogique : un outil en construction, qui évolue chaque semaine et s’inspire d’événements réels comme WannaCry pour rendre la cybersécurité plus concrète et accessible.
