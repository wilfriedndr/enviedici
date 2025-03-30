import graphviz
import os

# Définition du chemin d'enregistrement
output_dir = "D:/Desktop/code/Boutique angular django"
os.makedirs(output_dir, exist_ok=True)

# Création du schéma d'architecture
arch = graphviz.Digraph("Architecture", format='png')
arch.attr(rankdir="LR", fontsize='10')

# Frontend
arch.node("AngularApp", "Frontend Angular\n(vitrine + commandes)", shape="component", style="filled", fillcolor="#e3f2fd")
arch.node("DjangoAdmin", "Frontend Django\n(portail admin)", shape="component", style="filled", fillcolor="#ffe0b2")

# API Backend
arch.node("DjangoAPI", "Backend Django API\n(DRF)", shape="component", style="filled", fillcolor="#c8e6c9")

# Base de données
arch.node("PostgreSQL", "PostgreSQL\n(Base de données)", shape="cylinder", style="filled", fillcolor="#f8bbd0")

# Authentification
arch.node("JWT", "JWT\n(Authentication)", shape="note", style="filled", fillcolor="#d1c4e9")

# Tâches asynchrones
arch.node("Celery", "Celery\n(Tâches async)", shape="component", style="filled", fillcolor="#f0f4c3")
arch.node("Redis", "Redis\n(Broker Celery)", shape="component", style="filled", fillcolor="#dcedc8")

# Orchestration
arch.node("Docker", "Docker\n(Conteneurisation)", shape="box3d", style="filled", fillcolor="#b3e5fc")
arch.node("Kubernetes", "Kubernetes\n(Orchestration)", shape="box3d", style="filled", fillcolor="#b2dfdb")

# Relations
arch.edges([("AngularApp", "DjangoAPI"),
            ("DjangoAdmin", "DjangoAPI"),
            ("DjangoAPI", "PostgreSQL"),
            ("DjangoAPI", "JWT"),
            ("DjangoAPI", "Celery"),
            ("Celery", "Redis"),
            ("Docker", "AngularApp"),
            ("Docker", "DjangoAdmin"),
            ("Docker", "DjangoAPI"),
            ("Docker", "PostgreSQL"),
            ("Docker", "Celery"),
            ("Docker", "Redis"),
            ("Kubernetes", "Docker")])

# Rendu
arch.render("architecture_projet", directory=output_dir, cleanup=False)
f"{output_dir}/architecture_projet.png"
