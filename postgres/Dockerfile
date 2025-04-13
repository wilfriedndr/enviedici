FROM postgres:15

# Installer des extensions si besoin
RUN apt-get update && apt-get install -y postgresql-contrib

# Copier un fichier de config PostgreSQL personnalisé (optionnel)
COPY postgresql.conf /etc/postgresql/postgresql.conf

# Initialisation : les fichiers *.sql ou *.sh dans ce dossier sont lancés automatiquement
COPY init.sql /docker-entrypoint-initdb.d/init.sql
