# Pourquoi les ports sont la clé pour comprendre la cyberdéfense

*Cyberanalyste-Défensif — Article de fond*

## Le point de départ

Quand on commence en cyberdéfense, on est vite tenté de sauter directement vers des sujets impressionnants : le hacking, les malwares, l'intelligence artificielle appliquée à la sécurité. Mais tout ça repose sur une base beaucoup plus simple, et pourtant souvent négligée : **les ports**.

Un port, c'est une porte d'entrée et de sortie sur un appareil connecté à un réseau. Chaque service (un site web, un partage de fichiers, une base de données) utilise un port précis pour communiquer. Comprendre les ports, c'est comprendre littéralement **par où circulent les données**.

## Une progression logique

Partir des ports permet de construire une compréhension solide, étape par étape :

### 1. Connaître les ports
Savoir quels ports existent, à quoi ils servent, et lesquels sont ouverts sur un appareil donné. C'est la base : on ne peut pas protéger ce qu'on ne connaît pas.

### 2. Les utiliser
Comprendre comment les services légitimes s'en servent au quotidien (le web utilise le port 443, le partage de fichiers Windows utilise le port 445, etc.).

### 3. Les analyser
Observer et monitorer ce qui transite réellement par ces ports — pas juste en théorie, mais en pratique, avec des outils de journalisation (logs) et des filtres.

### 4. Les protéger
Une fois qu'on sait ce qui rentre et sort, on peut décider quoi bloquer, quoi permettre, et comment réduire les risques (fermer les ports inutiles, restreindre les accès, surveiller les anomalies).

## Pourquoi c'est une excellente école

Cette approche a un avantage clé : elle rend visible ce qui est normalement invisible. La plupart des gens utilisent Internet sans jamais se demander ce qui transite réellement par leur appareil. En observant directement le trafic par port, on développe un réflexe essentiel en cyberdéfense — **voir avant de réagir**.

De plus, cette base facilite la compréhension de tout ce qui vient après :
- Les couches applicatives (web, courriel, bases de données) prennent tout leur sens une fois qu'on sait par où elles transitent.
- Le modèle réseau (OSI/TCP-IP), souvent perçu comme abstrait, devient concret.
- Le filtrage et l'optimisation des flux deviennent des gestes naturels, pas des concepts théoriques.

## Un exemple concret : le port 445

Le port 445 (utilisé pour le partage de fichiers Windows, protocole SMB) est l'un des ports les plus ciblés au monde. Une analyse de Barracuda Networks a révélé que plus de 91% des attaques observées sur ce port tentaient d'exploiter la même faille — EternalBlue — qui a permis la propagation de WannaCry et NotPetya en 2017. Des chercheurs estiment que plus d'un million d'appareils connectés à Internet exposent encore ce port aujourd'hui, souvent sans que leurs propriétaires en soient conscients.

C'est un exemple parfait de pourquoi connaître ses propres ports ouverts n'est pas un exercice théorique : c'est une question de surface d'attaque réelle et mesurable.

## La suite logique de ce projet

Ce projet part des ports comme fil conducteur, avant d'aborder progressivement :
- Le monitoring et la journalisation du trafic réseau
- Le filtrage (pare-feu, règles d'accès)
- Les bonnes pratiques applicatives (au-dessus des ports)

Chaque étape s'appuie sur la précédente — exactement comme une vraie progression pédagogique en cyberdéfense.

---

*Cet article accompagne le script [`scan_ports.py`](../audit/scan_ports.py) de ce projet.*
