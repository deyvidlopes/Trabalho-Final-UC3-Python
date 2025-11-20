from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from django.contrib.auth import views as auth_views # Importa as views prontas
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Rota de Login (aponta para o nosso template que criaremos abaixo)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Rota de Logout (apenas desloga e redireciona)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Nova rota para detalhes (int:pk significa que esperamos um número inteiro)
    path('produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),
]