from django.urls import path
from . import views
from .views import CustomPasswordChangeView

urlpatterns = [
    path('', views.index, name='controle_acesso_index'),
    path('cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('perfil/', views.user_profile, name='perfil'),
    path('perfil/editar/', views.edit_profile, name='edit_profile'),
    path('check-password-change/', views.check_password_change, name='check_password_change'),
    path('trocar-senha/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('historico-atividades/',views.activity_log_view, name='user_activity_list'),
    path('set_group/<int:user_id>/', views.set_group, name='set_group'),
]