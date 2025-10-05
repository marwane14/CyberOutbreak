# 🧠💻 CyberOutbreak — simulateur pédagogique d’infections numériques

**CyberOutbreak** est un laboratoire pédagogique isolé qui simule, de façon abstraite et sûre,
la dynamique d’infections informatiques dans un réseau.  
Le projet modélise des agents adverses adaptatifs , l’apparition textuelle de failles ,
la création quotidienne d’hôtes ,le déploiement de correctifs et la réponse humaine.  
Aucune action réelle n’est effectuée sur des systèmes externes : tout est simulé.

---

## 🎯 Objectifs
- Rendre **observables** la propagation, la détection et la remédiation.  
- Étudier **l’impact** de la segmentation et des architectures réseau.  
- Évaluer **l’efficacité** des experts et contre-mesures automatisées.  
- Simuler le comportement d’**agents IA abstraits** récompensés pour découvertes et compromissions.  
- Sensibiliser aux **compromis opérationnels** (faux positifs, coûts, délais).

---

## 🧱 Principes de sécurité
- Simulation **strictement abstraite** (aucun exploit ni code réel).  
- **Aucune communication réseau** sortante activée par défaut.  
- Bouton d’arrêt d’urgence (**kill-switch**) pour désactiver les agents IA.  
- **Exécution isolée** conseillée (VM ou container sans accès externe).  

---

## ⚙️ Fonctionnalités principales
- Simulation **multi-agent** : hôtes, routeurs, attaquants, experts et IA abstraites.  
- **Cycle de vie** des hôtes : création journalière, durée de vie, retrait automatique.  
- **Failles textuelles** : gravité, découverte, patch et adoption progressive.  
- **Récompense dynamique** des agents selon compromissions et découvertes.  
- **Interface temps réel** : graphe réseau, indicateurs, courbes et journaux d’événements.  
- **Scénarios configurables** pour adapter les conditions de simulation.  
- Données enregistrées pour **analyse et reproductibilité**.

---

## 🧩 Modèle conceptuel
- **Host** : statut, profil, vulnérabilités textuelles, âge et connexions.  
- **Vulnerability** : gravité, état de patch, historique de découvertes.  
- **AiAgent** : paramètres internes, budget d’action, score de récompense.  
- **Actions abstraites** : reconnaissance, tentative d’exploitation, découverte, mouvement latéral.  
- **Système de récompense** : encourage adaptation, diversité et exploration sans attaques réelles.

---

## 📊 Journaux et données
- États simulés horodatés accessibles pour l’interface et l’analyse.  
- Séries temporelles : infections, alertes, patchs, récompenses cumulées.  
- Journal d’événements : découvertes, compromissions, mutations et correctifs.  
- Sauvegarde de **seeds** et logs pour la reproductibilité des expériences.

---

## 🌐 Visualisations clés
- Graphe réseau dynamique coloré selon état et profil.  
- Courbes temporelles du pourcentage d’infectés.  
- Barres ou histogrammes pour récompenses cumulées.  
- Arbre évolutif des agents IA montrant mutations et variantes.  
- Filtres interactifs pour explorer le journal par agent, hôte ou vulnérabilité.

---

## 🧪 Scénarios pédagogiques
- **Reconnaissance IA** : visibilité et inventaire réseau.  
- **Furtivité IA** : camouflage et détection comportementale.  
- **Adaptatif IA** : mutation face aux contre-mesures.  
- **Zero-Day abstrait** : montée temporaire du taux de succès d’exploitation.  

Chaque scénario est **entièrement simulé** et ne contient **aucune donnée réelle**.

---

## 🚀 Installation et exécution
1. Déployer le simulateur et l’interface dans un environnement isolé.  
2. Lancer séparément le **moteur de simulation** et l’**interface web**.  
3. Accéder à l’interface locale pour visualiser la simulation en temps réel.  
4. Charger un scénario pédagogique préconfiguré pour l’expérimentation.

---

## 🧠 Développement et structure
- Moteur de simulation, gestion des scénarios, IA abstraite et API web clairement séparés.  
- Répertoires dédiés aux scénarios, logs et données persistantes.  
- Structure pensée pour la **clarté, la sécurité et la reproductibilité**.  
- Tests unitaires recommandés pour toute contribution.

---

## 🤝 Contribution
- Ouvrir une **issue** pour signaler un bug ou proposer une idée.  
- Soumettre des **pull requests** avec documentation et tests.  
- Toute contribution doit rester **abstraite et non exécutoire**.

---

## ⚖️ Éthique et usage
- Usage **strictement pédagogique**.  
- Ne pas exécuter sur des environnements réels ou en production.  
- Revue éthique recommandée pour usages externes.  
- Partager les journaux et seeds uniquement dans le respect de la confidentialité.

---

## 🔮 Prochaines étapes
- Créer de nouveaux **scénarios guidés** pour l’enseignement.  
- Enrichir les **visualisations pédagogiques** et tableaux de bord.  
- Documenter davantage les **mécaniques d’évolution IA**.  
- Simplifier le déploiement pour les écoles et centres de formation.

---

🧠 CyberOutbreak vise à rendre la cybersécurité **visible, interactive et compréhensible**,  
sans jamais exécuter de risque réel.  
C’est un **bac à sable éducatif**, pensé pour observer, tester et apprendre.
