# 🚗 Smart Parking Management (Rennes Métropole)

> **Real-time visualization of park-and-ride occupancy.**
> A Python project illustrating the evolution of a solution: from raw algorithmic processing to the use of industry standards.

This project connects to the Rennes Métropole Open Data API to retrieve real-time parking data. It processes this information to generate an **interactive map** that allows users to instantly visualize parking availability through an intuitive color-coded system.

---

### Project Architecture: An Evolutionary Approach

This repository contains the different iterations of the project as well as the deployment configuration.

#### 1. `main.py` (Production Version - Recommended)
* **Concept:** Professional approach using standard libraries.
* **Technique:**
    * **JSON Parsing:** Uses the `json` module to transform the API response into Python data structures.
    * **Datetime:** Time manipulation via the `datetime` module for precise timestamping.
* **Advantage:** Robust, maintainable code that complies with industry standards. This is the main entry point.

#### 2. `manual_parsing.py` (Algorithmic Version)
* **Concept:** "Low-level" processing of raw data.
* **Technique:** Data is handled as a string. Extraction is performed through manual slicing algorithms.
* **Purpose:** Demonstrates the ability to manipulate raw data without an automatic parser.

#### 3. `Dockerfile` (Deployment) 🐳
* **Concept:** Isolated execution environment.
* **Technique:** Configuration script to containerize the application.
* **Purpose:** Ensures the code runs on any machine without requiring Python or the libraries to be pre-installed.

#### 4. `Map.Rennes.html`
* The output file: an interactive HTML map viewable in any web browser.

---

### Technical Overview

1.  **API Connection:** HTTP request via `requests` to the Rennes Open Data API (`tco-parcsrelais-star-etat-tr`).
2.  **Business Logic:**
    * Occupancy rate calculation: `(Max Capacity - Available Spots) / Max Capacity`.
3.  **Visualization Logic:**
    * 🟢 **Green:** Occupancy < 50%
    * 🟠 **Orange:** Occupancy between 50% and 80%
    * 🔴 **Red:** Occupancy > 80%
4.  **Geographic Rendering:** Dynamic markers (size proportional to occupancy rate) generated on an OpenStreetMap background using the **Folium** library.

---

### Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white) |
| **Data & API** | `Requests` `JSON` `Open Data API` |
| **Geolocation** | `Folium` (Leaflet.js wrapper) |
| **Deployment** | ![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=flat&logo=docker&logoColor=white) |

---

### Installation & Usage

You can run this project in two ways: using standard Python or via Docker (recommended for portability).

#### Option A: Standard Launch (Python)

1.  **Clone the repository:**
```bash
    git clone https://github.com/your-username/smart-parking-management.git
    cd smart-parking-management
```

2.  **Install dependencies:**
```bash
    pip install requests folium
```

3.  **Run the script:**
```bash
    python main.py
```

#### Option B: Docker Launch 🐳

This method does not require Python or the libraries to be installed on your machine.

1.  **Build the image:**
```bash
    docker build -t parking-rennes .
```

2.  **Run the container:**
```bash
    docker run --rm -v ${PWD}:/app parking-rennes
```
    *(This command mounts the volume so that the `Map.Rennes.html` file is generated directly in your current folder).*

---
#### 👁️ Result
In both cases, open the generated `Map.Rennes.html` file in your preferred web browser to view the map.

---
*Nolan Nedelec - Developed as part of the ISEN Ouest engineering curriculum.*
