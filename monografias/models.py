from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('ADMIN', 'Administrador'),
        ('PROF', 'Professor'),
        ('ALUNO', 'Aluno'),
    ]
    tipo_usuario = models.CharField(max_length=5, choices=TIPO_USUARIO_CHOICES, default='ALUNO')

    # Removido método save sobrescrito para não duplicar criptografia de senha

class Equipe(models.Model):
    usuario = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200)
    
    FA_CHOICES = [
        ("G", "Graduação"),
        ("M", "Mestrado"),
        ("D", "Doutorado"),
    ]
    
    formacao = models.CharField(max_length=30, choices=FA_CHOICES, default="G")
    email = models.EmailField(max_length=100, null=True, blank=True)
    registro_criado = models.DateTimeField(auto_now_add=True)
    registro_atualizado = models.DateTimeField(auto_now=True)

    # Campos de URL agora são CharField
    lattes = models.CharField(max_length=500, null=True, blank=True)
    google_scholar = models.CharField(max_length=500, null=True, blank=True)
    research_gate = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    orcid = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)

    pdf = models.FileField(upload_to='equipes/pdfs/', null=True, blank=True)
   
    def __str__(self):
        return self.nome

