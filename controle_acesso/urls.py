from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='controle_acesso_index'),  # Página inicial do controle de acesso
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
]
