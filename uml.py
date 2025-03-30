from graphviz import Digraph

# Création d'un nouveau diagramme UML mis à jour avec RapportVente historisé
uml_updated = Digraph("UML_Model_Full", format='png')
uml_updated.attr(rankdir="LR")

# Entités
uml_updated.node("Producteur", """Producteur
- id
- nom
- description
- localisation
- photo
- date_ajout""")

uml_updated.node("Produit", """Produit
- id
- nom
- description
- prix
- stock_disponible
- photo
- actif
- date_ajout
- producteur_id""")

uml_updated.node("Client", """Client
- id
- nom
- email
- téléphone
- adresse_retrait
- date_inscription""")

uml_updated.node("Commande", """Commande
- id
- client_id
- date_commande
- statut
- total
- créneau_retrait_id""")

uml_updated.node("CommandeProduit", """CommandeProduit
- commande_id
- produit_id
- quantité
- prix_unitaire""")

uml_updated.node("Créneau", """Créneau
- id
- jour
- heure_debut
- heure_fin
- disponible
- capacité_max""")

uml_updated.node("PériodeFermeture", """PériodeFermeture
- id
- date_debut
- date_fin
- motif""")

uml_updated.node("RapportVente", """RapportVente
- id
- date_rapport
- date_debut
- date_fin
- total_ventes
- nb_commandes
- pdf_path""")

# Relations
uml_updated.edge("Producteur", "Produit", label="1 → *")
uml_updated.edge("Produit", "CommandeProduit", label="1 → *")
uml_updated.edge("Client", "Commande", label="1 → *")
uml_updated.edge("Commande", "CommandeProduit", label="1 → *")
uml_updated.edge("Commande", "Créneau", label="* → 1")
uml_updated.edge("CommandeProduit", "Produit", label="* → 1")

uml_updated.render("uml_model", directory="D:/Desktop/code/Boutique angular django", cleanup=False)
