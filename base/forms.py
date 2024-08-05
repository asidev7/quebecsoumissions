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




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
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
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'ville': forms.TextInput(attrs={'class': 'form-control'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'description_courte': forms.Textarea(attrs={'class': 'form-control'}),
            'site_web': forms.URLInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'derniere_realisation': forms.Textarea(attrs={'class': 'form-control'}),
            'texte_presentation': forms.Textarea(attrs={'class': 'form-control'}),
            'avantages': forms.Textarea(attrs={'class': 'form-control'}),
            'courte_description_seo': forms.Textarea(attrs={'class': 'form-control'}),
            'courte_description_entreprise': forms.Textarea(attrs={'class': 'form-control'}),
            'code_promotionnel': forms.TextInput(attrs={'class': 'form-control'}),
            'pourcentage_remise': forms.NumberInput(attrs={'class': 'form-control'}),
            'conditions_acceptees': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'page_presentation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'forfait': forms.Select(attrs={'class': 'form-control'}),
        }




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('adresse', 'code_postal', 'numero_telephone', 'conditions_acceptees')
