#!/bin/sh

echo "Attente de PostgreSQL..."

while ! nc -z postgres 5432; do
  sleep 1
done

echo "PostgreSQL est prêt, on lance les migrations"

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn django_backend.wsgi:application --bind 0.0.0.0:8000
