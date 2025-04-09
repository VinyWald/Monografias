from django.forms import ModelForm
from . models import Equipe

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = "__all__"