from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def welcome_api(request):
    return JsonResponse({"message": "Bienvenue sur l’API Django 🎉"})

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', welcome_api),
]
