from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import GerenteCadastroForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'controle_acesso/index.html')

def is_admin(user):
    return user.is_staff


@login_required
@user_passes_test(is_admin)
def cadastro_usuario(request):
    if request.method == 'POST':
        form = GerenteCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = GerenteCadastroForm()
    return render(request, 'controle_acesso/cadastro_usuario.html', {'form':form})
    
@login_required
@user_passes_test(is_admin)
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request,'controle_acesso/lista_usuarios.html', {'usuarios':usuarios})