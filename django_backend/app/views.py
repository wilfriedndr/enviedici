from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



choix_par_page = [10, 25, 50, 100]

def welcome_api(request):
    return JsonResponse({"message": "Bienvenue sur l’API Django 🎉"})

def is_gerant(user):
    return user.is_authenticated and user.is_gerant

@login_required
@user_passes_test(is_gerant)
def home_gerant_view(request):
    return render(request, "backoffice/home.html")

@login_required
@user_passes_test(is_gerant)
def produits_vue_gerant(request):
    producteur_id = request.GET.get("producteur")
    par_page = request.GET.get("par_page", 10)
    tous_les_producteurs = Producteur.objects.all()

    if producteur_id:
        produits = Produit.objects.filter(producteur_id=producteur_id)
    else:
        produits = Produit.objects.all()

    paginator = Paginator(produits, par_page)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "produits/liste_produits.html", {
        "page_obj": page_obj,
        "producteurs": tous_les_producteurs,
        "producteur_id": int(producteur_id) if producteur_id else None,
        "par_page": int(par_page),
        "choix_par_page": choix_par_page,
    })


def login_gerant_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_gerant:
            login(request, user)
            return redirect("backoffice_home")
        else:
            error = "Identifiants invalides ou vous n’êtes pas un gérant."
            return render(request, "backoffice/login.html", {"error": error})

    return render(request, "backoffice/login.html")

@require_POST
@login_required
@user_passes_test(is_gerant)
def logout_gerant_view(request):
    logout(request)
    return redirect('login_gerant')

@login_required
@user_passes_test(is_gerant)
@require_http_methods(["GET", "POST"])
def ajouter_produit_view(request):
    producteurs = Producteur.objects.all()

    if request.method == "POST":
        nom = request.POST.get("nom")
        description = request.POST.get("description")
        prix = request.POST.get("prix")
        stock = request.POST.get("quantite_stock")
        photo = request.FILES.get("image")
        producteur_id = request.POST.get("producteur")

        try:
            producteur = Producteur.objects.get(id=producteur_id)
        except Producteur.DoesNotExist:
            return render(request, "produits/ajouter_produit.html", {
                "error": "Producteur invalide.",
                "producteurs": producteurs
            })

        if nom and prix and stock:
            Produit.objects.create(
                nom=nom,
                description=description,
                prix=prix,
                stock_disponible=stock,
                photo=photo,
                producteur=producteur
            )
            return redirect("gerant_produits")

        return render(request, "produits/ajouter_produit.html", {
            "error": "Tous les champs obligatoires doivent être remplis.",
            "producteurs": producteurs
        })

    return render(request, "produits/ajouter_produit.html", {"producteurs": producteurs})

@login_required
@user_passes_test(is_gerant)
def modifier_produit_view(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == "POST":
        produit.nom = request.POST.get("nom")
        produit.description = request.POST.get("description")
        produit.prix = request.POST.get("prix")
        produit.quantite_stock = request.POST.get("quantite_stock")

        if request.FILES.get("image"):
            produit.image = request.FILES["image"]

        produit.save()
        return redirect("gerant_produits")

    return render(request, "produits/modifier_produit.html", {"produit": produit})

@login_required
@user_passes_test(is_gerant)
def supprimer_produit_produit_view(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == "POST":
        quantite_supprimee = request.POST.get("quantite")
        if quantite_supprimee == "tous":
            produit.delete()
            return redirect("gerant_produits")
        else:
            try:
                q = int(quantite_supprimee)
                if q >= produit.quantite_stock:
                    produit.delete()
                else:
                    produit.quantite_stock -= q
                    produit.save()
            except ValueError:
                pass  # mauvaise saisie = on ignore

        return redirect("gerant_produits")

    return render(request, "produits/supprimer_produit.html", {"produit": produit})

@login_required
@user_passes_test(is_gerant)
def liste_producteurs_view(request):
    producteurs = Producteur.objects.all()
    return render(request, "producteurs/liste_producteurs.html", {"producteurs": producteurs})

@login_required
@user_passes_test(is_gerant)
@require_http_methods(["GET", "POST"])
def ajouter_producteur_view(request):
    if request.method == "POST":
        try:
            nom = request.POST.get("nom")
            description = request.POST.get("description")
            localisation = request.POST.get("localisation")
            photo = request.FILES.get("photo")

            if not all([nom, description, localisation, photo]):
                raise ValueError("Tous les champs sont obligatoires.")

            Producteur.objects.create(
                nom=nom,
                description=description,
                localisation=localisation,
                photo=photo
            )

            return redirect("liste_producteurs")
        
        except Exception as e:
            print("⚠️ Erreur lors de l’ajout du producteur :", e)
            return render(request, "producteurs/add_producteur.html", {
                "error": f"Une erreur s’est produite : {e}"
            })

    return render(request, "producteurs/add_producteur.html")

@login_required
@user_passes_test(is_gerant)
@require_http_methods(["GET", "POST"])
def modifier_producteur_view(request, producteur_id):
    producteur = get_object_or_404(Producteur, id=producteur_id)

    if request.method == "POST":
        producteur.nom = request.POST.get("nom")
        producteur.description = request.POST.get("description")
        producteur.localisation = request.POST.get("localisation")

        if request.FILES.get("photo"):
            producteur.photo = request.FILES["photo"]

        producteur.save()
        return redirect("liste_producteurs")

    return render(request, "producteurs/change_producteur.html", {"producteur": producteur})

@login_required
@user_passes_test(is_gerant)
@require_http_methods(["GET", "POST"])
def supprimer_producteur_view(request, producteur_id):
    producteur = get_object_or_404(Producteur, id=producteur_id)
    produits_associes = producteur.produits.all()

    if request.method == "POST":
        confirm = request.POST.get("confirm")
        if confirm == "oui":
            producteur.delete()
            return redirect("liste_producteurs")
        else:
            return redirect("liste_producteurs")

    return render(request, "producteurs/supprimer_producteur.html", {
        "producteur": producteur,
        "produits_associes": produits_associes
    })
