from django.shortcuts import render
from . models import Equipe
from . forms import EquipeForm

# Create your views here.

def index(request):
    equipe =Equipe.objects.all()
    context ={
        'lista':equipe
    }
    return render(request,'equipe.html',context)

def adc(request):
    form=EquipeForm()
    if request.method == "POST":
        form=EquipeForm(request.POST)
        
        if form.is_valid():
            post = form.save()
            post.save()
            form = EquipeForm()
            return render(request, "adc_equipe.html",{'form':form})
        else:
            form=EquipeForm()
    return render(request, "adc_equipe.html",{'form':form})