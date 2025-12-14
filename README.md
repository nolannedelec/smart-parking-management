# Smart Parking Management (Rennes Métropole)

> **Visualisation en temps réel de l'occupation des parcs-relais.**
> Un projet Python illustrant l'évolution d'une solution : du traitement algorithmique brut à l'utilisation des standards industriels.

Ce projet se connecte à l'API Open Data de Rennes Métropole pour récupérer les données de stationnement en temps réel. Il traite ces informations pour générer une **carte interactive** permettant aux usagers de visualiser instantanément la disponibilité des places via un code couleur intuitif.

---

### Architecture du Projet : Une approche évolutive

Ce dépôt contient deux versions du script, conservées pour démontrer la progression technique et la compréhension des différentes méthodes de traitement de données.

#### 1. `main.py` (Version Production - Recommandée) 
* **Concept :** Approche professionnelle utilisant les bibliothèques standards.
* **Technique :**
    * **JSON Parsing :** Utilisation du module `json` pour transformer la réponse API en structures de données Python (dictionnaires/listes).
    * **Datetime :** Manipulation temporelle via le module `datetime` pour un horodatage précis.
* **Avantage :** Code robuste, maintenable et conforme aux standards de l'industrie. C'est le point d'entrée principal du projet.

#### 2. `manual_parsing.py` (Version Algorithmique) 
* **Concept :** Traitement "bas niveau" des données brutes.
* **Technique :** Les données de l'API sont traitées comme une chaîne de caractères brute (`string`). L'extraction des informations se fait via des algorithmes de découpage et de recherche de motifs, sans utiliser de parseur JSON automatique.
* **Objectif :** Démontrer la capacité à manipuler des données brutes et à construire une logique d'extraction manuelle.

#### 3. `Map.Rennes.html` 🗺️
* Le fichier de sortie généré par le script : une carte HTML interactive visualisable dans n'importe quel navigateur web.

---

### Fonctionnement Technique

1.  **Connexion API :** Requête HTTP via `requests` vers l'API Open Data de Rennes (`tco-parcsrelais-star-etat-tr`).
2.  **Calculs Métiers :**
    * Calcul du taux d'occupation : `(Capacité Max - Places Dispo) / Capacité Max`.
3.  **Logique de Visualisation :**
    * 🟢 **Vert :** Remplissage < 50%
    * 🟠 **Orange :** Remplissage entre 50% et 80%
    * 🔴 **Rouge :** Remplissage > 80%
4.  **Rendu Géographique :** Génération de marqueurs dynamiques (taille proportionnelle au taux de remplissage) sur fond OpenStreetMap via la bibliothèque **Folium**.

---

### 🛠️ Stack Technique

| Catégorie | Technologies |
| :--- | :--- |
| **Langage** | ![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white) |
| **Flux de Données** | `Requests` `JSON` `Open Data API` |
| **Géolocalisation** | `Folium` (Leaflet.js wrapper) |
| **Traitement** | `Datetime` `String Manipulation` |

---

### Installation & Utilisation

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/ton-pseudo/smart-parking-management.git](https://github.com/ton-pseudo/smart-parking-management.git)
    cd smart-parking-management
    ```

2.  **Installer les dépendances :**
    ```bash
    pip install requests folium
    ```

3.  **Lancer l'application :**
    ```bash
    python main.py
    ```
    *Le script va récupérer les dernières données et générer/mettre à jour le fichier `Map.Rennes.html`.*

4.  **Visualiser le résultat :**
    Ouvrez le fichier `Map.Rennes.html` généré avec votre navigateur web préféré (Chrome, Firefox, Edge...).

---
*Nedelec Nolan - Développé dans le cadre du cursus ingénieur ISEN Ouest.*
