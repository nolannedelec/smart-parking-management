# 1. On part d'une version légère de Linux avec Python 3.10 installé
FROM python:3.10-slim

# 2. On empêche Python de garder des fichiers en cache (pour voir les logs en direct)
ENV PYTHONUNBUFFERED=1

# 3. On crée un dossier de travail "/app" à l'intérieur du conteneur
WORKDIR /app

# 4. On installe les bibliothèques nécessaires (requests et folium)
RUN pip install --no-cache-dir requests folium

# 5. On copie TOUS tes fichiers (.py, .html, etc.) dans le conteneur
COPY . .

# 6. La commande qui se lance au démarrage : on exécute ton script principal
CMD ["python", "main.py"]