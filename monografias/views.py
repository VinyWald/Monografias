from django.shortcuts import render
from .models import Monografias

# Create your views here.
def index(request):
    monografias =Monografias.objects.all()
    context ={
        'lista':monografias
    }
    return render(request,'monografias.html',context)