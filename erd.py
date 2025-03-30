import graphviz

# Création du diagramme ERD mis à jour
erd = graphviz.Digraph("ERD_Model", format='png')
erd.attr(rankdir="LR")

# Entités avec attributs principaux (ERD style)
erd.node("Producteur", shape="record", label="{Producteur|+ id : PK\\l+ nom\\l+ description\\l+ localisation\\l+ photo\\l+ date_ajout\\l}")
erd.node("Produit", shape="record", label="{Produit|+ id : PK\\l+ nom\\l+ description\\l+ prix\\l+ stock_disponible\\l+ photo\\l+ actif\\l+ date_ajout\\l+ producteur_id : FK\\l}")
erd.node("Client", shape="record", label="{Client|+ id : PK\\l+ nom\\l+ email\\l+ téléphone\\l+ adresse_retrait\\l+ date_inscription\\l}")
erd.node("Commande", shape="record", label="{Commande|+ id : PK\\l+ client_id : FK\\l+ date_commande\\l+ statut\\l+ total\\l+ créneau_retrait_id : FK\\l}")
erd.node("CommandeProduit", shape="record", label="{CommandeProduit|+ commande_id : FK\\l+ produit_id : FK\\l+ quantité\\l+ prix_unitaire\\l}")
erd.node("Créneau", shape="record", label="{Créneau|+ id : PK\\l+ jour\\l+ heure_debut\\l+ heure_fin\\l+ disponible\\l+ capacité_max\\l}")
erd.node("PériodeFermeture", shape="record", label="{PériodeFermeture|+ id : PK\\l+ date_debut\\l+ date_fin\\l+ motif\\l}")
erd.node("RapportVente", shape="record", label="{RapportVente|+ id : PK\\l+ date_rapport\\l+ date_debut\\l+ date_fin\\l+ total_ventes\\l+ nb_commandes\\l+ pdf_path\\l}")

# Relations
erd.edge("Producteur", "Produit", label="1 → *")
erd.edge("Produit", "CommandeProduit", label="1 → *")
erd.edge("Client", "Commande", label="1 → *")
erd.edge("Commande", "CommandeProduit", label="1 → *")
erd.edge("Commande", "Créneau", label="* → 1")
erd.edge("CommandeProduit", "Produit", label="* → 1")

erd.render("erd_model", directory="D:/Desktop/code/Boutique angular django", cleanup=False)