from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Equipe
import re

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'tipo_usuario']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuário'}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-select'}),
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        exclude = ['usuario', 'registro_criado', 'registro_atualizado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'formacao': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'lattes': forms.URLInput(attrs={'class': 'form-control'}),
            'google_scholar': forms.URLInput(attrs={'class': 'form-control'}),
            'research_gate': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'orcid': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_google_scholar(self):
        url = self.cleaned_data.get('google_scholar')
        if url:
            # Valida se começa com http ou https
            if not re.match(r'^https?://', url):
                raise forms.ValidationError("A URL deve começar com http:// ou https://")
        return url
