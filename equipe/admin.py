from django.contrib import admin

# Register your models here.

from . models import Equipe
class EquipeAdmin(admin.ModelAdmin):
    readonly_fields = ["registro_criado", "registro_atualizado"]

admin.site.register(Equipe,EquipeAdmin)