from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_gerant = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Producteur(TimeStampedModel):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    localisation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="producteurs/")
    date_ajout = models.DateField(auto_now_add=True)

class Produit(TimeStampedModel):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock_disponible = models.PositiveIntegerField()
    photo = models.ImageField(upload_to="produits/")
    actif = models.BooleanField(default=True)
    date_ajout = models.DateField(auto_now_add=True)
    producteur = models.ForeignKey(Producteur, on_delete=models.CASCADE, related_name="produits")

class Client(TimeStampedModel):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    téléphone = models.CharField(max_length=20)
    adresse_retrait = models.CharField(max_length=255)
    date_inscription = models.DateField(auto_now_add=True)

class Créneau(TimeStampedModel):
    jour = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    disponible = models.BooleanField(default=True)
    capacité_max = models.PositiveIntegerField()

class Commande(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="commandes")
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    créneau_retrait = models.ForeignKey(Créneau, on_delete=models.SET_NULL, null=True, related_name="commandes")

    # Paiement
    mode_paiement = models.CharField(
        max_length=20,
        choices=[('en_ligne', 'En ligne'), ('sur_place', 'Sur place')],
        default='sur_place'
    )
    # Paiement
    date_paiement = models.DateTimeField(null=True, blank=True)
    # Retrait
    date_retrait_effectif = models.DateTimeField(null=True, blank=True)
    # PDF Facture
    pdf_facture = models.FileField(upload_to="factures/", null=True, blank=True)
    
class StatutCommandeHistorique(TimeStampedModel):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="historiques_statut")
    statut = models.CharField(max_length=50)
    date_changement = models.DateTimeField(auto_now_add=True)

class CommandeProduit(TimeStampedModel):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name="produits_commandés")
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantité = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

class PériodeFermeture(TimeStampedModel):
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()

class RapportVente(TimeStampedModel):
    date_rapport = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    total_ventes = models.DecimalField(max_digits=12, decimal_places=2)
    nb_commandes = models.PositiveIntegerField()
    pdf_path = models.FileField(upload_to="rapports/")

