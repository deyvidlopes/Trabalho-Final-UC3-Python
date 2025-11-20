from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Produto

def index(request):
    # Pega todos os produtos inicialmente
    produtos = Produto.objects.all()
    
    # Lógica de Filtro (Item 8 - Listagens com filtros)
    busca = request.GET.get('busca')
    if busca:
        # Filtra se o nome conter o termo digitado (icontains ignora maiúscula/minúscula)
        produtos = produtos.filter(nome__icontains=busca)

    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

from django.shortcuts import render, get_object_or_404 # Importe o get_object_or_404
from .models import Produto

# ... (sua view index já existente)

def detalhe_produto(request, pk):
    # Busca o produto pelo ID (pk) ou retorna erro 404 se não achar
    produto = get_object_or_404(Produto, pk=pk)
    
    context = {
        'produto': produto
    }
    return render(request, 'detalhe_produto.html', context)