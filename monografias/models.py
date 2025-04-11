from django.db import models
from equipe.models import Equipe

# Create your models here.

class Monografias(models.Model):
    titulo=models.CharField(max_length=250)
    
    discente=models.OneToOneField(Equipe,on_delete=models.CASCADE)
    
    orientador=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,blank=True,related_name="orientador")
    
    coorientador=models.ForeignKey(Equipe,on_delete=models.CASCADE,null=True,blank=True,related_name="coorientador")
    
    data=models.DateField(null=True,blank=True)

    
    def __str__(self):
        return self.titulo
    