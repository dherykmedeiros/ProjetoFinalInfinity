from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gestao_recursos_index'),  # Página inicial da gestão de recursos
]
