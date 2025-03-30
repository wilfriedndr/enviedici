# README Technique – Projet Boutique Angular + Django

## ✨ Présentation du projet

Ce projet vise à développer une application web pour une épicerie locale mettant en avant des produits du terroir. Il comprend :

- Une **vitrine/boutique en ligne** pour les clients (Angular)
- Un **portail d'administration** pour le personnel (Django)
- Une **API REST** centralisée (Django REST Framework)
- Une **base de données relationnelle PostgreSQL**
- Une **architecture conteneurisée avec Docker** et orchestrable via **Kubernetes**

---

## 📁 Arborescence des applications

```
Boutique angular django/
├── angular-app/            # Frontend vitrine
├── django-admin/           # Interface admin Django
├── django-api/             # Backend Django (API REST)
├── docker/                 # Fichiers Docker (Dockerfile, compose, etc.)
├── architecture_projet.png # Schéma d'architecture
├── uml_model_full.png      # Schéma UML du modèle de données
├── erd_model_full.png      # Schéma ERD de la base de données
└── README.md               # Ce fichier
```

---

## 🛠️ Stack technique

### Frontend

- Angular 17 (vitrine + achat)
- Django templates (interface admin)

### Backend

- Django 5
- Django REST Framework (API REST)

### Base de données

- PostgreSQL 15

### Infrastructure

- Docker pour la conteneurisation
- Kubernetes pour l'orchestration (optionnel mais prévu)
- Celery + Redis pour les tâches asynchrones
- JWT pour l'authentification

---

## 📊 Fonctionnalités principales

### Côté Client (Angular)

- Consultation des producteurs locaux
- Navigation dans la vitrine (produits)
- Commande en ligne (panier, stock, retrait en créneau)
- Authentification (JWT)

### Côté Admin (Django)

- Gestion des stocks & produits
- Suivi des commandes et créneaux
- Configuration du calendrier (fermetures)
- Génération de rapports PDF (via Celery)

---

## 🧱 Roadmap technique

### Mise en place initiale

-

### Infrastructure

-

### Services asynchrones

-

---

## ⚠️ Sécurité & bonnes pratiques

- Authentification via JWT (Angular <-> API)
- Hash des mots de passe (Django default)
- Stockage des variables sensibles dans des secrets (env / Kubernetes config)
- Gestion des droits : utilisateur / admin (Group/Permission Django)

---

## 📅 Sauvegarde automatique BDD

- Planifiée via `cron` ou `k8s CronJob`
- Utilisation de `pg_dump`
- Volume persistant pour stocker les dumps
- Possibilité d'envoi vers un cloud (S3, etc.) en option

---

## 🌐 Accès futur / Déploiement

- Accès possible via NGINX / Ingress (K8s)
- Utilisation de certificats SSL (Let's Encrypt, Traefik, etc.)
- CI/CD possible via GitHub Actions ou GitLab CI

---

## 📃 Schémas

- `architecture_projet.png` : Vue globale du projet
- `uml_model_full.png` : Modèle de données objet (UML)
- `erd_model_full.png` : Modèle relationnel (ERD)

---

> Projet développé par **Wilfried NIEDERHOFFER** — Concepteur développeur d'applications.

