from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from base.models import Fonctionnalite, Forfait, Information, Realisation, Service, Type_Soumission,Blog

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom') 
admin.site.register(Service, ServiceAdmin)

# Register your models here.
class AdminTypeSoummission(admin.ModelAdmin):
    list_display = ('id', 'nom') 

admin.site.register(Type_Soumission, AdminTypeSoummission)

class AdminInformation(admin.ModelAdmin):
    list_display = ('id', 'nom','logo','adresse', 'numero_telephone') 

admin.site.register(Information, AdminInformation)

class AdminForfait(admin.ModelAdmin):
    list_display = ('id','nom_forfait')

admin.site.register(Forfait, AdminForfait)

@admin.register(Blog)
class BlogAdmin(MarkdownxModelAdmin):
    list_display = ('titre', 'auteur', 'date_publiaction', 'slug')
    prepopulated_fields = {'slug': ('titre',)}


admin.site.register(Fonctionnalite)
admin.site.register(Realisation)