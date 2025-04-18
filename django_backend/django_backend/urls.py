from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

API_VERSION = "v1"

urlpatterns = [
    path(f'api/{API_VERSION}/admin/', admin.site.urls),  # accès Django admin
    path(f'api/{API_VERSION}/', include("app.urls")),    # toutes les routes de l'app
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)