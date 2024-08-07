from django import forms
from .models import Soumission
from .models import Entreprise
from django.contrib.auth.models import User
from .models import Entreprise
from django.contrib.auth.models import User
from .models import Entreprise
from django import forms
from .models import Client


class SoumissionForm(forms.ModelForm):
    class Meta:
        model = Soumission
        fields = ['type_soummission', 'adresse', 'ville', 'code_postal', 'numero_telephone', 'description_travaux']
        widgets = {
            'type_soummission': forms.Select(attrs={'class': 'form-control p-3'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Entrez votre adresse'}),
            'ville': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Entrez votre ville'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Entrez votre code postal'}),
            'numero_telephone': forms.TextInput(attrs={'class': 'form-control p-3', 'placeholder': 'Entrez votre numéro de téléphone'}),
            'description_travaux': forms.Textarea(attrs={'class': 'form-control p-3', 'placeholder': 'Décrivez les travaux'}),
        }
        help_texts = {
            'type_soummission': 'Choisissez le type de soumission',
            'adresse': 'Entrez l\'adresse complète où les travaux doivent être effectués',
            'ville': 'Entrez la ville',
            'code_postal': 'Entrez le code postal',
            'numero_telephone': 'Entrez un numéro de téléphone où nous pouvons vous joindre',
            'description_travaux': 'Décrivez en détail les travaux à réaliser',
        }


from django import forms
from django.contrib.auth.models import User
from .models import Entreprise

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre mot de passe'}),
        label='Mot de passe'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre nom d\'utilisateur'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'}),
        }
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Email',
            'password': 'Mot de passe'
        }

class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = [
            'service',
            'adresse',
            'ville',
            'code_postal',
            'numero_telephone',
            'latitude',
            'longitude',
            'description_courte',
            'site_web',
            'logo',
            'derniere_realisation',
            'texte_presentation',
            'avantages',
            'courte_description_seo',
            'courte_description_entreprise',
            'forfait',
            'page_presentation',
            'code_promotionnel',
            'pourcentage_remise',
            'conditions_acceptees'
        ]
        widgets = {
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre adresse'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre ville'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre code postal'}),
            'numero_telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez la longitude'}),
            'description_courte': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez une description courte'}),
            'site_web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Entrez l\'URL de votre site web'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'derniere_realisation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Décrivez votre dernière réalisation'}),
            'texte_presentation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez le texte de présentation'}),
            'avantages': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Listez les avantages'}),
            'courte_description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez une description courte pour le SEO'}),
            'courte_description_entreprise': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entrez une description courte de l\'entreprise'}),
            'code_promotionnel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le code promotionnel'}),
            'pourcentage_remise': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le pourcentage de remise'}),
            'conditions_acceptees': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'page_presentation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'forfait': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'service': 'Service',
            'adresse': 'Adresse',
            'ville': 'Ville',
            'code_postal': 'Code postal',
            'numero_telephone': 'Numéro de téléphone',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'description_courte': 'Description courte',
            'site_web': 'Site web',
            'logo': 'Logo',
            'derniere_realisation': 'Dernière réalisation',
            'texte_presentation': 'Texte de présentation',
            'avantages': 'Avantages',
            'courte_description_seo': 'Description courte pour le SEO',
            'courte_description_entreprise': 'Description courte de l\'entreprise',
            'code_promotionnel': 'Code promotionnel',
            'pourcentage_remise': 'Pourcentage de remise',
            'conditions_acceptees': 'Conditions acceptées',
            'page_presentation': 'Page de présentation',
            'forfait': 'Forfait'
        }


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['adresse', 'code_postal', 'numero_telephone', 'conditions_acceptees']
        widgets = {
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre adresse'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre code postal'}),
            'numero_telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre numéro de téléphone'}),
            'conditions_acceptees': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'adresse': 'Adresse',
            'code_postal': 'Code postal',
            'numero_telephone': 'Numéro de téléphone',
            'conditions_acceptees': 'Conditions acceptées'
        }