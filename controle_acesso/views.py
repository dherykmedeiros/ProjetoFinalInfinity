from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import GerenteCadastroForm, EditProfileForm, SetGroupForm
from .models import Profile, UserActivity
from django.views.generic import ListView
from django.core.paginator import Paginator


# Função de view para a página inicial
def index(request):
    return render(request, 'controle_acesso/index.html')

# Funções para validação de acesso
def is_admin(user):
    return user.is_superuser

def is_manager_adm(user):
    return user.is_superuser or user.groups.filter(name='Gerente').exists()

# Cadastro de usuário para administradores
@login_required
@user_passes_test(is_admin, login_url='/acesso')
def cadastro_usuario(request):
    if request.method == 'POST':
        form = GerenteCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = GerenteCadastroForm()
    return render(request, 'controle_acesso/cadastro_usuario.html', {'form': form})

# Lista de usuários para administradores e gerentes
@login_required
@user_passes_test(is_manager_adm)
def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'controle_acesso/lista_usuarios.html', {'usuarios': usuarios})

# Edição de perfil de usuário
@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'controle_acesso/edit_profile.html', {'form': form})

# Visualização do perfil do usuário
@login_required
def user_profile(request):
    return render(request, 'controle_acesso/user_profile.html', {'user': request.user})

# Verificação para redirecionar se a senha precisa ser trocada
@login_required
def check_password_change(request):
    if request.user.is_superuser:
        return redirect('perfil')  # Superuser vai direto para o perfil
    elif request.user.profile.must_change_password:
        return redirect('change_password')  # Outros usuários com `must_change_password=True` são redirecionados para trocar a senha
    else:
        return redirect('perfil')

# View customizada de troca de senha com atualização de status de troca
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'controle_acesso/change_password.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Atualiza o campo must_change_password
        self.request.user.profile.must_change_password = False
        self.request.user.profile.save()
        return response


# class UserActivityListView(ListView):
#     model = UserActivity
#     template_name = 'controle_acesso/user_activity_list.html'
#     context_object_name = 'activities'
#     ordering = ['-timestamp']
#     paginate_by = 10
@login_required
@user_passes_test(is_admin)
def activity_log_view(request):
    activities_list = UserActivity.objects.select_related('user').order_by('-timestamp')
    paginator = Paginator(activities_list, 10)  # Mostra 10 atividades por página

    page_number = request.GET.get('page')
    activities = paginator.get_page(page_number)

    return render(request, 'controle_acesso/user_activity_list.html', {'activities': activities})

@login_required
@user_passes_test(is_manager_adm)
def set_group(request, user_id):
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        form = SetGroupForm(request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = SetGroupForm(user=user)
    
    return render(request, 'controle_acesso/set_group.html', {'form': form, 'user': user})