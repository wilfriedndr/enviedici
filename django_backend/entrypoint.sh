#!/bin/bash

# Appliquer les migrations
echo "➤ Applying database migrations..."
python manage.py migrate --noinput

# Collecter les fichiers statiques
echo "➤ Collecting static files..."
python manage.py collectstatic --noinput

# Lancer Gunicorn
echo "➤ Starting Gunicorn server..."
exec gunicorn django_backend.wsgi:application --bind 0.0.0.0:8000
