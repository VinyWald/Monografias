from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Equipe, CustomUser
from .forms import EquipeForm, UserRegistrationForm

def is_admin(user):
    return user.tipo_usuario == 'ADMIN'

def is_professor(user):
    return user.tipo_usuario == 'PROF'

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
@login_required
def index(request):
    user = request.user
    context = {
        'user': user,
        'tipo_usuario': user.tipo_usuario,
    }
    return render(request, 'dashboard.html', context)


@login_required
@user_passes_test(is_admin)
def list(request):
    equipe = Equipe.objects.all()
    context = {'lista': equipe}
    return render(request, 'list.html', context)

@login_required
@user_passes_test(lambda u: is_admin(u) or is_professor(u))
@login_required
def adc(request):
    if request.method == "POST":
        equipe_form = EquipeForm(request.POST, request.FILES)
        if equipe_form.is_valid():
            equipe = equipe_form.save(commit=False)
            equipe.usuario = request.user  # associa ao usuário logado
            equipe.save()
            messages.success(request, "Equipe adicionada com sucesso.")
            return redirect('list')
    else:
        equipe_form = EquipeForm()

    return render(request, "adc_equipe.html", {
        'equipe_form': equipe_form,
    })


@login_required
@user_passes_test(is_admin)
def equipe_update(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        form = EquipeForm(request.POST, request.FILES, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EquipeForm(instance=equipe)
    return render(request, 'form.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def equipe_delete(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    if request.method == 'POST':
        equipe.delete()
        return redirect('list')
    return render(request, 'delete.html', {'equipe': equipe})

@login_required
def detalhes(request, pk):
    equipe = get_object_or_404(Equipe, pk=pk)
    return render(request, 'detalhes.html', {'equipe': equipe})

def registro_publico(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'cadastro.html', {'form': form})
