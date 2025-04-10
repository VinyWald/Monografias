from datetime import date
from django.http import Http404
from django.shortcuts import render
from .models import Monografias

# Create your views here.
def index(request):
    if request.method=='POST':
        dados=request.POST.copy()
        
        inicio=int(dados['ano_inicial'])
        fim=int(dados['ano_final'])
        monografias=Monografias.objects.filter(data__range=(date(inicio,1,1),date(fim,12,31)))
    else:
        monografias =Monografias.objects.all()
    context ={
        'lista':monografias
    }
    return render(request,'monografias.html',context)

def detalhes(request,pk):
    print("Primary Key {}".format(pk))
    try:
        monografias=Monografias.objects.filter(pk=pk)
        print(monografias.values())
    except monografias.DoesNotExist:
        raise Http404('Monografia Não Existe')
    
    context={
        'monografias':monografias
    }
    return render(request,'detalhes.html',context)