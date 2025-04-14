from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_client', 'is_proprietaire', 'is_staff', 'is_active')
    list_filter = ('is_client', 'is_proprietaire', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Rôles', {'fields': ('is_client', 'is_proprietaire')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rôles', {'fields': ('is_client', 'is_proprietaire')}),
    )
