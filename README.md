<h1 align="center">💻🦠 CyberOutbreak</h1>
<p align="center">
  <img src="https://raw.githubusercontent.com/marwane14/CyberOutbreak/main/ui/static/logo.gif" width="120" alt="logo animation">
</p>
<p align="center">
  <b>Un simulateur pédagogique d’infections numériques évolutives</b><br>
  <i>Observer. Comprendre. Défendre.</i>
</p>

---

## 🎯 Objectif

CyberOutbreak transforme la cybersécurité en une **expérience interactive et visuelle**.  
Chaque seconde, des ordinateurs simulés se connectent, s’infectent, se protègent et s’adaptent.  
Le tout sans aucun code dangereux — tout est **100% abstrait et éducatif**.

---

## ⚙️ Fonctionnement visuel

| Élément | Représentation | Description |
|----------|----------------|-------------|
| 🟢 Hôte sain | Vert | Machine fonctionnelle et protégée |
| 🔴 Infecté | Rouge clignotant (animé via GIF) | Contaminé par le virus simulé |
| 🟣 Expert | Violet | Détecte et corrige les infections |
| ⚫ IA attaquante | Noir pulsant | Agent abstrait apprenant à infecter |
| 💾 Patch | Icône bouclier 🛡️ | Corrige une faille après découverte |
| 🧬 Mutation IA | GIF de réseau neuronal animé | Montre l’évolution de la stratégie |

*(tu peux remplacer ces GIF par de vraies animations locales dans ton dossier `/ui/static/`)*

---

## 🧠 Principe général

🎮 **Une simulation, pas une attaque :**
- Les virus et failles sont des *objets virtuels*, non du code exécutable.  
- Les IA reçoivent des **récompenses** (score) pour explorer et “infecter” dans l’environnement simulé.  
- Les experts humains ou automatiques cherchent à **endiguer la propagation**.

🕸️ **Cycle complet :**
1. De nouvelles machines apparaissent chaque jour.  
2. Des failles émergent aléatoirement.  
3. Les agents IA tentent des infections virtuelles.  
4. Les experts publient des patchs.  
5. Le réseau s’équilibre, puis recommence.

---

## 📊 Visualisations (en direct dans l’UI)

<p align="center">
  <img src="https://raw.githubusercontent.com/marwane14/CyberOutbreak/main/ui/static/network_anim.gif" width="500"><br>
  <i>Exemple de carte réseau animée (Cytoscape.js)</i>
</p>

- **Carte réseau** 🕸️ : visualise chaque hôte, ses connexions et son état.  
- **Courbes d’évolution** 📈 : taux d’infection, progression des patchs, score IA.  
- **Histogrammes dynamiques** 📊 : vulnérabilités découvertes par type.  
- **Timeline des événements** ⏱️ : infections, patchs, mutations.

---

## 🔬 Scénarios pédagogiques

| Scénario | Description | Compétence mise en avant |
|-----------|--------------|---------------------------|
| 🤖 IA Reconnaissance | L’IA explore le réseau | Visibilité & inventaire |
| 🕶️ IA Furtive | Attaque lente et silencieuse | Détection comportementale |
| 🧬 IA Adaptative | Mutation progressive | Résilience et réponse adaptative |
| ⚡ Zero-Day abstrait | Nouvelle faille inattendue | Gestion de crise & patching |

---

## 💾 Architecture simplifiée

🧱 **Backend (Python)**  
→ Gère la logique du réseau et écrit les fichiers d’état.  

🌐 **Serveur web (Flask)**  
→ Diffuse les données via flux SSE en temps réel.  

🧭 **Interface (HTML + Tailwind + JS)**  
→ Utilise Cytoscape.js pour le graphe et Chart.js pour les graphiques.  

🗂️ **Scénarios YAML**  
→ Permettent de modifier la taille du réseau, les probabilités, ou les comportements IA.

---

## ⚖️ Éthique et sécurité

🚫 Aucun code réel d’exploitation.  
🧩 Simulation 100 % déconnectée.  
🧑‍🏫 Usage uniquement éducatif.  
🔒 Recommandé : exécution dans une VM sans réseau.  

> CyberOutbreak n’est **pas un outil d’attaque**, mais un **outil de sensibilisation**.

---

## 🪄 En résumé

> 🔥 CyberOutbreak, c’est **la cybersécurité rendue visible**.  
> 🧠 Les virus apprennent.  
> 👨‍💻 Les humains réparent.  
> 🛡️ Et tout se joue dans un monde entièrement simulé.

---

<p align="center">
  <img src="https://raw.githubusercontent.com/marwane14/CyberOutbreak/main/ui/static/footer_anim.gif" width="120">
  <br>
  <sub>© Projet éducatif CyberOutbreak — Simulation purement abstraite</sub>
</p>
