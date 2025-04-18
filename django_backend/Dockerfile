FROM python:3.12.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Collecte des fichiers statiques (si tu veux que les fichiers statiques soient dispos)
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Autorise le passage du header Authorization
CMD ["gunicorn", "django_backend.wsgi:application", "--bind", "0.0.0.0:8000", "--env", "WSGIPassAuthorization=true"]
