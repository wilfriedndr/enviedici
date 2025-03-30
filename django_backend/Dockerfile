# Base Python officielle (version récente)
FROM python:3.12-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copier tout le reste du projet
COPY . .

# Exposer le port Django
EXPOSE 8000

# Commande par défaut (modifiable via docker-compose)
# CMD ["gunicorn", "django_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
ENTRYPOINT ["./entrypoint.sh"]
