from django import forms
from .models import Funcionario, Treinamento, Equipamento, AreaRestrita, ControleAcesso, RelatorioIncidente, ManutencaoEquipamento, Veiculo, ControleVeiculo

# Formulário para o modelo Funcionario
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['usuario', 'turno', 'qualificacoes', 'nivel_acesso', 'data_admissao']

# Formulário para o modelo Treinamento
class TreinamentoForm(forms.ModelForm):
    class Meta:
        model = Treinamento
        fields = ['funcionario', 'nome', 'descricao', 'data', 'validade']

# Formulário para o modelo Equipamento
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ['tipo', 'localizacao', 'status', 'ultima_manutencao', 'descricao']

# Formulário para o modelo AreaRestrita
class AreaRestritaForm(forms.ModelForm):
    class Meta:
        model = AreaRestrita
        fields = ['nome', 'descricao', 'monitoramento_ativo']

# Formulário para o modelo ControleAcesso
class ControleAcessoForm(forms.ModelForm):
    class Meta:
        model = ControleAcesso
        fields = ['usuario', 'area_restrita']

# Formulário para o modelo RelatorioIncidente
class RelatorioIncidenteForm(forms.ModelForm):
    class Meta:
        model = RelatorioIncidente
        fields = ['funcionario', 'descricao', 'data_incidente', 'resolvido', 'data_resolucao']

# Formulário para o modelo ManutencaoEquipamento
class ManutencaoEquipamentoForm(forms.ModelForm):
    class Meta:
        model = ManutencaoEquipamento
        fields = ['equipamento', 'data_manutencao', 'detalhes']

# Formulário para o modelo Veiculo
class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'modelo', 'status', 'ultima_manutencao']

# Formulário para o modelo ControleVeiculo
class ControleVeiculoForm(forms.ModelForm):
    class Meta:
        model = ControleVeiculo
        fields = ['veiculo', 'funcionario', 'data_saida', 'data_retorno', 'observacoes']
