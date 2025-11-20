from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- PÁGINA INICIAL ---
    path('', views.index, name='index'),

    # --- PRODUTOS ---
    path('produto/<int:pk>/', views.detalhe_produto, name='detalhe_produto'),

    # --- USUÁRIOS (LOGIN/CADASTRO) ---
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),

    # --- CARRINHO DE COMPRAS ---
    path('adicionar-carrinho/<int:pk>/', views.adicionar_carrinho, name='add_carrinho'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('remover-carrinho/<int:pk>/', views.remover_carrinho, name='remove_carrinho'),
]