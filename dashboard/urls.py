from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),  # Página inicial do dashboard
]
