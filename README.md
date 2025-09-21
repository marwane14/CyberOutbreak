# CyberOutbreak 🦠💻

**CyberOutbreak** est un laboratoire pédagogique qui simule la propagation d’une « infection » dans un réseau informatique.  
L’objectif est de montrer comment différents facteurs (architecture, profils utilisateurs, présence d’un VPN, interventions humaines ou IA) influencent la vitesse et l’ampleur de la propagation.

---

## 🎯 Objectifs
- Comprendre les analogies entre virus biologiques et infections numériques.  
- Montrer l’importance de l’architecture réseau et de la segmentation.  
- Comparer l’efficacité de différents profils (expert, novice, absent) et d’une assistance par IA.  
- Fournir un outil simple et visuel pour sensibiliser à la cybersécurité.

---

## ⚙️ Fonctionnalités
- Simulation d’un réseau de machines avec profils variés (expert, novice, absent).  
- Paramètres configurables : probabilité de propagation, présence d’un VPN, vitesse d’infection.  
- Visualisation en temps réel via une interface web (Flask).  
- Génération d’indicateurs : nombre d’hôtes infectés, pourcentage d’infection, temps jusqu’au containment.  
- Extensible : possibilité d’ajouter de nouveaux scénarios (OT, segmentation, etc.).

---

## 🚀 Installation et exécution

### 1. Cloner le projet
```bash
git clone https://github.com/marwane14/CyberOutbreak.git
cd CyberOutbreak
