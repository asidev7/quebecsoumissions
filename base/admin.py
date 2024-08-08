from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Client, Entreprise, Fonctionnalite, Forfait, Information, Realisation, Service, Soumission, Type_Soumission, Blog

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
admin.site.register(Service, ServiceAdmin)

class AdminTypeSoumission(admin.ModelAdmin):
    list_display = ('id', 'nom')
admin.site.register(Type_Soumission, AdminTypeSoumission)

class AdminInformation(admin.ModelAdmin):
    list_display = ('id', 'nom', 'logo', 'adresse', 'numero_telephone')
admin.site.register(Information, AdminInformation)

class AdminForfait(admin.ModelAdmin):
    list_display = ('id', 'nom_forfait')
admin.site.register(Forfait, AdminForfait)

@admin.register(Blog)
class BlogAdmin(MarkdownxModelAdmin):
    list_display = ('titre', 'auteur', 'date_publiaction', 'slug')
    prepopulated_fields = {'slug': ('titre',)}
    
admin.site.register(Fonctionnalite)
admin.site.register(Realisation)
admin.site.register(Entreprise)
admin.site.register(Client)
admin.site.register(Soumission)