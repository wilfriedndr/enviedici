from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome_api, name='welcome'),
    path('backoffice/login/', login_gerant_view, name='login_gerant'),
    path('backoffice/produits/', produits_vue_gerant, name='gerant_produits'),
    path('backoffice/home', home_gerant_view, name='backoffice_home'),
    path('backoffice/logout/', logout_gerant_view, name='logout_gerant'),
    path('backoffice/produits/ajouter/', ajouter_produit_view, name='ajouter_produit'),
    path('backoffice/produits/modifier/<int:produit_id>/', modifier_produit_view, name='modifier_produit'),
    path('backoffice/produits/supprimer/<int:produit_id>/', supprimer_produit_produit_view, name='supprimer_produit_produit'),
    path('backoffice/producteurs/', liste_producteurs_view, name='liste_producteurs'),
    path('backoffice/producteurs/ajouter/', ajouter_producteur_view, name='ajouter_producteur'),
    path("backoffice/producteurs/modifier/<int:producteur_id>/", modifier_producteur_view, name="modifier_producteur"),
    path("backoffice/producteurs/supprimer/<int:producteur_id>/", supprimer_producteur_view, name="supprimer_producteur"),

]
