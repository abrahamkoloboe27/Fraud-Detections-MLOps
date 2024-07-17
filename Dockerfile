# Utiliser l'image Python officielle
FROM python:3.8-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "api/app.py"]
