from django.shortcuts import get_object_or_404, redirect, render
from . models import Equipe
from . forms import EquipeForm

# Create your views here.

def index(request):
    equipe =Equipe.objects.all()
    context ={
        'lista':equipe
    }
    return render(request,'equipe.html',context)

def list(request):
    equipe =Equipe.objects.all()
    context ={
        'lista':equipe
    }
    return render(request,'list.html',context)
def adc(request):
    equipe = Equipe.objects.all()
    context = {
        'lista': equipe
    }

    if request.method == "POST":
        form = EquipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "equipe.html", context)
        else:
            print(form.errors)  # Isso ajuda na depuração, pode remover depois
    else:
        form = EquipeForm()
    
    return render(request, "adc_equipe.html", {'form': form})


def equipe_update(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    equipel =Equipe.objects.all()
    context ={
        'lista':equipel
    }
    if request.method == 'POST':
        form = EquipeForm(request.POST, request.FILES, instance=equipe)
        if form.is_valid():
            form.save()
            return render(request, "list.html",context)
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'form.html', {'form': form})

def equipe_delete(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    equipel =Equipe.objects.all()
    context ={
        'lista':equipel
    }
    if request.method == 'POST':
        equipe.delete()
        return render(request, "list.html",context)
    return render(request, 'delete.html')