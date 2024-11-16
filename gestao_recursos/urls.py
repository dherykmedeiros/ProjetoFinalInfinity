from django.urls import path
from . import views


urlpatterns = [
    # URLs para Funcionario
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/criar/', views.criar_funcionario, name='criar_funcionario'),
    path('funcionarios/<int:id>/editar/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/<int:id>/excluir/', views.excluir_funcionario, name='excluir_funcionario'),

    # URLs para Treinamento
    path('treinamentos/', views.lista_treinamentos, name='lista_treinamentos'),
    path('treinamentos/criar/', views.criar_treinamento, name='criar_treinamento'),
    

    # URLs para Equipamento
    path('equipamentos/', views.lista_equipamentos, name='lista_equipamentos'),
    path('equipamentos/criar/', views.criar_equipamento, name='criar_equipamento'),
    

    # URLs para AreaRestrita
    path('areas_restritas/', views.lista_areas_restritas, name='lista_areas_restritas'),
    path('areas_restritas/criar/', views.criar_area_restrita, name='criar_area_restrita'),


    # URLs para RelatorioIncidente
    path('incidentes/', views.lista_incidentes, name='lista_incidentes'),
    path('incidentes/criar/', views.criar_incidente, name='criar_incidente'),
    

    # URLs para Veiculo
    path('veiculos/', views.lista_veiculos, name='lista_veiculos'),
    path('veiculos/criar/', views.criar_veiculo, name='criar_veiculo'),
   

    # URLs para ControleVeiculo
    path('controle_veiculos/', views.lista_controle_veiculos, name='lista_controle_veiculos'),
    path('controle_veiculos/criar/', views.criar_controle_veiculo, name='criar_controle_veiculo'),
   
    path('', views.index, name='gestao_recursos_index'),  # Página inicial da gestão de recursos
]

