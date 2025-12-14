# 🚗 Smart Parking Management (Rennes Métropole)

> **Visualisation en temps réel de l'occupation des parcs-relais.**
> Un projet Python illustrant l'évolution d'une solution : du traitement algorithmique brut à l'utilisation des standards industriels.

Ce projet se connecte à l'API Open Data de Rennes Métropole pour récupérer les données de stationnement en temps réel. Il traite ces informations pour générer une **carte interactive** permettant aux usagers de visualiser instantanément la disponibilité des places via un code couleur intuitif.

---

### Architecture du Projet : Une approche évolutive

Ce dépôt contient les différentes itérations du projet ainsi que la configuration de déploiement.

#### 1. `main.py` (Version Production - Recommandée)
* **Concept :** Approche professionnelle utilisant les bibliothèques standards.
* **Technique :**
    * **JSON Parsing :** Utilisation du module `json` pour transformer la réponse API en structures de données Python.
    * **Datetime :** Manipulation temporelle via le module `datetime` pour un horodatage précis.
* **Avantage :** Code robuste, maintenable et conforme aux standards. C'est le point d'entrée principal.

#### 2. `manual_parsing.py` (Version Algorithmique)
* **Concept :** Traitement "bas niveau" des données brutes.
* **Technique :** Les données sont traitées comme une chaîne de caractères (`string`). L'extraction se fait via des algorithmes de découpage manuels.
* **Objectif :** Démontrer la capacité à manipuler des données brutes sans parseur automatique.

#### 3. `Dockerfile` (Déploiement) 🐳
* **Concept :** Environnement d'exécution isolé.
* **Technique :** Script de configuration pour conteneuriser l'application.
* **Objectif :** Garantir que le code fonctionne sur n'importe quelle machine sans installation préalable de Python ou des bibliothèques.

#### 4. `Map.Rennes.html`
* Le fichier de sortie : une carte HTML interactive visualisable dans n'importe quel navigateur.

---

### Fonctionnement Technique

1.  **Connexion API :** Requête HTTP via `requests` vers l'API Open Data de Rennes (`tco-parcsrelais-star-etat-tr`).
2.  **Calculs Métiers :**
    * Calcul du taux d'occupation : `(Capacité Max - Places Dispo) / Capacité Max`.
3.  **Logique de Visualisation :**
    * 🟢 **Vert :** Remplissage < 50%
    * 🟠 **Orange :** Remplissage entre 50% et 80%
    * 🔴 **Rouge :** Remplissage > 80%
4.  **Rendu Géographique :** Génération de marqueurs dynamiques (taille proportionnelle au taux) sur fond OpenStreetMap via la bibliothèque **Folium**.

---

### Stack Technique

| Catégorie | Technologies |
| :--- | :--- |
| **Langage** | ![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white) |
| **Data & API** | `Requests` `JSON` `Open Data API` |
| **Géolocalisation** | `Folium` (Leaflet.js wrapper) |
| **Déploiement** | ![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=flat&logo=docker&logoColor=white) |

---

### Installation & Utilisation

Vous pouvez lancer ce projet de deux manières : via Python classique ou via Docker (recommandé pour la portabilité).

#### Option A : Lancement Standard (Python)

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/ton-pseudo/smart-parking-management.git](https://github.com/ton-pseudo/smart-parking-management.git)
    cd smart-parking-management
    ```

2.  **Installer les dépendances :**
    ```bash
    pip install requests folium
    ```

3.  **Lancer le script :**
    ```bash
    python main.py
    ```

#### Option B : Lancement via Docker 🐳

Cette méthode ne nécessite pas d'installer Python ou les librairies sur votre machine.

1.  **Construire l'image :**
    ```bash
    docker build -t parking-rennes .
    ```

2.  **Lancer le conteneur :**
    ```bash
    docker run --rm -v ${PWD}:/app parking-rennes
    ```
    *(Cette commande monte le volume pour que le fichier `Map.Rennes.html` soit généré directement dans votre dossier actuel).*

---
#### 👁️ Résultat
Dans les deux cas, ouvrez le fichier `Map.Rennes.html` généré avec votre navigateur web préféré pour consulter la carte.

---
*Nolan Nedelec - Développé dans le cadre du cursus ingénieur ISEN Ouest.*
