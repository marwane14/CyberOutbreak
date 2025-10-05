## CyberOutbreak — simulateur pédagogique d’infections numériques

CyberOutbreak est un laboratoire pédagogique isolé qui simule, de façon abstraite et sûre, la dynamique d’infections informatiques dans un réseau.
Le projet modélise des agents adverses adaptatifs, l’apparition textuelle de failles, la création quotidienne d’hôtes, le déploiement de correctifs et la réponse humaine. Rien n’agit sur des systèmes réels. Tout est représenté par des objets et des événements simulés.

## Objectifs

Rendre observables la propagation, la détection et la remédiation.

Étudier l’impact des architectures réseau et de la segmentation.

Évaluer l’efficacité des experts et des contre-mesures automatisées.

Explorer le comportement d’agents IA abstraits récompensés pour découvertes et compromissions.

Sensibiliser aux compromis opérationnels (coût des réponses, faux positifs).

## Principes de sécurité

Simulation strictement abstraite. Aucun exploit ou code réel.

Aucune communication réseau sortante activée par défaut.

Kill-switch pour désactiver les agents IA.

Exécution recommandée en environnement isolé (VM/container) pour la sécurité.

## Fonctionnalités principales

Simulation multi-agent intégrant hôtes, routeurs, attaquants, experts et agents IA abstraits.

Modèle de vie des hôtes : création journalière, durée de vie, retrait.

Failles représentées par labels textuels avec gravité, découverte et patching simulés.

Récompense d’agents pour compromission et découverte de vulnérabilités (modélisé).

Patching et adoption progressifs selon profils d’utilisateurs.

Écriture atomique d’états et de métriques pour l’interface temps réel.

Interface web interactive avec graphe réseau, courbes temporelles et journal d’événements.

Scénarios configurables et reproductibles pour ateliers pédagogiques.

## Modèle conceptuel (haut niveau)

Host : entité contenant statut, vulnérabilités textuelles, profil et métadonnées temporelles.

Vulnerability : identité textuelle, gravité, état de patch, historique de découvertes.

AiAgent : représentation numérique (paramètres), budget d’action, historique de récompenses.

Actions : opérations abstraites (reconnaissance, tentative d’exploitation probabiliste, découverte, déplacement latéral).

Reward system : mécanique de récompense pour guider les stratégies sans exécuter d’attaques réelles.

## Flux de données et journaux

États synthétiques horodatés exposés pour l’UI et l’analyse.

Séries temporelles pour métriques (infectés, patchs, alertes, récompenses).

Journal d’événements structuré listant découvertes, compromissions, patchs et mutations.

Seeds RNG et logs d’expérimentation pour assurer reproductibilité.

## Visualisations clés

Graphe réseau dynamique coloré par statut et profil.

Courbe temporelle du pourcentage d’infectés.

Barres ou histogrammes pour récompenses cumulées et types de vulnérabilités.

Vue « arbre évolutif » pour variants d’agents et mutations.

Filtre de journal pour recherche par agent, vulnérabilité, hôte ou période.

## Scénarios pédagogiques recommandés

Reconnaissance IA : met l’accent sur l’inventaire et la visibilité.

Furtivité IA : met en évidence l’intérêt des baselines comportementales.

Adaptatif IA : montre la dynamique de mutation face aux contre-mesures.

Incident « zero-day » abstrait : simule une hausse ponctuelle de succès d’exploitation pour tester playbooks.

## Installation et exécution (vue générale)

Déployer le simulateur et l’interface dans un environnement isolé.

Lancer le moteur de simulation et l’interface web en processus séparés pour découpler calcul et UI.

Ouvrir l’interface locale pour visualiser la simulation en temps réel.

Utiliser des scénarios prédéfinis pour reproduire ateliers et exercices.

## Développement et structure (vue d’ensemble)

Modules séparés pour le moteur, la gestion des scénarios, le pool de vulnérabilités, les agents IA et l’API d’interface.

Répertoire dédié aux scénarios et aux logs d’expérimentation.

Tests unitaires pour la logique de simulation exigés pour toute contribution.

## Contribution

Ouvrir une issue pour bugs ou suggestions.

Proposer des PRs avec tests et documentation.

Toute contribution doit respecter l’obligation de rester abstraite et non-exécutoire.

## Éthique et usage

Usage strictement pédagogique et en environnement contrôlé.

Ne pas exécuter en production ni sur des réseaux réels.

Revue éthique recommandée pour usages hors contexte éducatif.

Conserver et partager seeds et logs uniquement si compatibles avec la politique de confidentialité locale.

## Prochaines étapes

Ajouter scénarios guidés pour ateliers.

Enrichir visualisations pédagogiques.
