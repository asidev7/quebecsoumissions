from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from slugger import AutoSlugField
from markdownx.models import MarkdownxField
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Information(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo")
    adresse = models.TextField()
    email = models.EmailField()
    numero_telephone = models.CharField(max_length=20)

class Service(models.Model):
    nom = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.nom
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

class Fonctionnalite(models.Model):
    nom = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Fonctionnalité'
        verbose_name_plural = 'Fonctionnalités'

class Forfait(models.Model):
    ABONNEMENT_CHOICES = [
        ('gratuit', 'Inscription GRATUITE'),
        ('visibilite_web', 'Forfait visibilité web '),
        ('strategie_marketing', 'Forfait stratégie marketing'),
        ('developpement_affaires', 'Forfait développement des affaires'),
    ]

    nom_forfait = models.CharField(max_length=255)
    prix_abonnement = models.PositiveBigIntegerField()
    type_abonnement = models.CharField(max_length=30, choices=ABONNEMENT_CHOICES)
    fonctionnalites = models.ManyToManyField(Fonctionnalite, blank=True)

    def __str__(self):
        return self.nom_forfait

    class Meta:
        verbose_name = 'Forfait'
        verbose_name_plural = 'Forfaits'


class Entreprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255,blank=True)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    numero_telephone = models.CharField(max_length=20)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description_courte = models.TextField()
    site_web = models.URLField()
    logo = models.ImageField(upload_to='logos/')
    derniere_realisation = models.TextField()
    texte_presentation = models.TextField()
    avantages = models.TextField()
    courte_description_seo = models.TextField()
    courte_description_entreprise = models.TextField()
    forfait = models.ForeignKey(Forfait, on_delete=models.SET_NULL, null=True)

    page_presentation = models.BooleanField(default=False)
    code_promotionnel = models.CharField(max_length=50, blank=True, null=True)
    pourcentage_remise = models.IntegerField(default=10)
    conditions_acceptees = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.site_web
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

   

    class Meta:
        verbose_name = 'Entrepreneur'
        verbose_name_plural = 'Entrepreneurs'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=10)
    numero_telephone = models.CharField(max_length=20)
    conditions_acceptees = models.BooleanField(default=False)

    
    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Type_Soumission(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nom
    class Meta:
        verbose_name = 'Type de soumission'
        verbose_name_plural = 'Type de soumission'



class Soumission(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    type_soummission = models.ForeignKey(Type_Soumission,on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    numero_telephone = models.CharField(max_length=20)
    description_travaux = models.TextField()
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Soumission de {self.user.username} à {self.adresse}"



class Realisation(models.Model):
    photo = models.ImageField(upload_to="Galleries")
    titre = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Realisations'


class Blog(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    contenu = RichTextField()
    auteur = models.CharField(max_length=255)
    date_publiaction = models.DateField(auto_now=True)
    slug = AutoSlugField(populate_from='titre', unique=True)

    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
        
class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    date_contact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact de {self.nom} pour {self.entreprise.nom}"