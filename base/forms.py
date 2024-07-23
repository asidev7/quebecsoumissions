from django import forms
from .models import Soumission

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
