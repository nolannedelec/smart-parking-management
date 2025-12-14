FROM python:3.10-slim
#On empêche Python de garder des fichiers en cache
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --no-cache-dir requests folium
COPY . .
CMD ["python", "main.py"]
