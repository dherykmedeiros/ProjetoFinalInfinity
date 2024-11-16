from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Funcionario, Treinamento, Equipamento, AreaRestrita, ControleAcesso, RelatorioIncidente, ManutencaoEquipamento, Veiculo, ControleVeiculo
from .forms import FuncionarioForm, TreinamentoForm, EquipamentoForm, AreaRestritaForm, ControleAcessoForm, RelatorioIncidenteForm, ManutencaoEquipamentoForm, VeiculoForm, ControleVeiculoForm

# Função auxiliar para verificar se o usuário está no grupo "Segurança"
def is_security(user):
    return user.groups.filter(name="Segurança").exists()

# VIEWS PARA FUNCIONÁRIOS

@login_required
@user_passes_test(is_security)
def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'gestao_recursos/funcionarios/lista_funcionarios.html', {'funcionarios': funcionarios})

@login_required
@user_passes_test(is_security)
def criar_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm()
    return render(request, 'gestao_recursos/funcionarios/criar_funcionario.html', {'form': form})

@login_required
@user_passes_test(is_security)
def editar_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('lista_funcionarios')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'gestao_recursos/funcionarios/editar_funcionario.html', {'form': form})

@login_required
@user_passes_test(is_security)
def excluir_funcionario(request, id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('lista_funcionarios')
    return render(request, 'gestao_recursos/funcionarios/excluir_funcionario.html', {'funcionario': funcionario})

# VIEWS PARA TREINAMENTOS

@login_required
@user_passes_test(is_security)
def lista_treinamentos(request):
    treinamentos = Treinamento.objects.all()
    return render(request, 'gestao_recursos/treinamentos/lista_treinamentos.html', {'treinamentos': treinamentos})

@login_required
@user_passes_test(is_security)
def criar_treinamento(request):
    if request.method == 'POST':
        form = TreinamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_treinamentos')
    else:
        form = TreinamentoForm()
    return render(request, 'gestao_recursos/treinamentos/criar_treinamento.html', {'form': form})

# Views para edição e exclusão de treinamento seriam similares, com `TreinamentoForm`

# VIEWS PARA EQUIPAMENTOS

@login_required
@user_passes_test(is_security)
def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'gestao_recursos/equipamentos/lista_equipamentos.html', {'equipamentos': equipamentos})

@login_required
@user_passes_test(is_security)
def criar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipamentos')
    else:
        form = EquipamentoForm()
    return render(request, 'gestao_recursos/equipamentos/criar_equipamento.html', {'form': form})

# VIEWS PARA ÁREAS RESTRITAS

@login_required
@user_passes_test(is_security)
def lista_areas_restritas(request):
    areas = AreaRestrita.objects.all()
    return render(request, 'gestao_recursos/areas_restritas/lista_areas_restritas.html', {'areas': areas})

@login_required
@user_passes_test(is_security)
def criar_area_restrita(request):
    if request.method == 'POST':
        form = AreaRestritaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_areas_restritas')
    else:
        form = AreaRestritaForm()
    return render(request, 'gestao_recursos/areas_restritas/criar_area_restrita.html', {'form': form})

# VIEWS PARA RELATÓRIOS DE INCIDENTES

@login_required
@user_passes_test(is_security)
def lista_incidentes(request):
    incidentes = RelatorioIncidente.objects.all()
    return render(request, 'gestao_recursos/incidentes/lista_incidentes.html', {'incidentes': incidentes})

@login_required
@user_passes_test(is_security)
def criar_incidente(request):
    if request.method == 'POST':
        form = RelatorioIncidenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_incidentes')
    else:
        form = RelatorioIncidenteForm()
    return render(request, 'gestao_recursos/incidentes/criar_incidente.html', {'form': form})

# VIEWS PARA VEÍCULOS

@login_required
@user_passes_test(is_security)
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'gestao_recursos/veiculos/lista_veiculos.html', {'veiculos': veiculos})

@login_required
@user_passes_test(is_security)
def criar_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm()
    return render(request, 'gestao_recursos/veiculos/criar_veiculo.html', {'form': form})

# VIEWS PARA CONTROLE DE USO DE VEÍCULOS

@login_required
@user_passes_test(is_security)
def lista_controle_veiculos(request):
    controles = ControleVeiculo.objects.all()
    return render(request, 'gestao_recursos/controle_veiculos/lista_controle_veiculos.html', {'controles': controles})

@login_required
@user_passes_test(is_security)
def criar_controle_veiculo(request):
    if request.method == 'POST':
        form = ControleVeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_controle_veiculos')
    else:
        form = ControleVeiculoForm()
    return render(request, 'gestao_recursos/controle_veiculos/criar_controle_veiculo.html', {'form': form})


def index(request):
    return render(request,"gestao_recursos/index.html")
