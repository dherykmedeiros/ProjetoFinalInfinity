from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin/', admin.site.urls),
    path('acesso/', include('controle_acesso.urls')),
    path('recursos/', include('gestao_recursos.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='controle_acesso/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'),name='logout')
    
]
