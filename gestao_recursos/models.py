from django.db import models
from django.contrib.auth import get_user_model

# Utilizando o modelo de usuário do controle_acesso
User = get_user_model()

# Modelo Funcionario (utilizando User do app controle_acesso)
class Funcionario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    turno = models.CharField(max_length=50)
    qualificacoes = models.TextField()
    nivel_acesso = models.CharField(max_length=50)
    data_admissao = models.DateField()

    def __str__(self):
        return self.usuario.username

# Modelo Treinamento para certificações dos funcionários
class Treinamento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="treinamentos")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateField()
    validade = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.funcionario.usuario.username}"

# Modelo Equipamento para recursos de segurança
class Equipamento(models.Model):
    TIPO_EQUIPAMENTO_CHOICES = [
        ('Câmera', 'Câmera'),
        ('Alarme', 'Alarme'),
        ('Comunicação', 'Comunicação'),
        ('Controle de Acesso', 'Controle de Acesso'),
        ('Detecção', 'Detecção'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_EQUIPAMENTO_CHOICES)
    localizacao = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    ultima_manutencao = models.DateField()
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.localizacao}"

# Modelo AreaRestrita para gerenciar áreas restritas
class AreaRestrita(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    monitoramento_ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

# Modelo ControleAcesso para registros de acesso às áreas restritas
class ControleAcesso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    area_restrita = models.ForeignKey(AreaRestrita, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.area_restrita.nome} em {self.data_acesso}"

# Modelo RelatorioIncidente para relatórios de incidentes
class RelatorioIncidente(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()
    data_incidente = models.DateTimeField()
    resolvido = models.BooleanField(default=False)
    data_resolucao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Incidente em {self.data_incidente} - {'Resolvido' if self.resolvido else 'Pendente'}"

# Modelo ManutencaoEquipamento para gerenciar manutenções de equipamentos
class ManutencaoEquipamento(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_manutencao = models.DateField()
    detalhes = models.TextField()

    def __str__(self):
        return f"{self.equipamento.tipo} - Manutenção em {self.data_manutencao}"

# Modelo Veiculo para gerenciar veículos de segurança
class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    ultima_manutencao = models.DateField()

    def __str__(self):
        return f"{self.modelo} - {self.placa}"

# Modelo ControleVeiculo para registros de uso dos veículos
class ControleVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_saida = models.DateTimeField()
    data_retorno = models.DateTimeField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.veiculo.modelo} - Saída em {self.data_saida}"
