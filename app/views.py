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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm # Importe o formulário pronto
from .models import Produto

# ... (suas views index e detalhe_produto) ...

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Vai para o login após criar conta
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'cadastro.html', context)

def adicionar_carrinho(request, pk):
    # Pega o carrinho da sessão ou cria lista vazia
    carrinho = request.session.get('carrinho', [])
    
    # Adiciona se não existir
    if pk not in carrinho:
        carrinho.append(pk)
        
    # Salva na sessão
    request.session['carrinho'] = carrinho
    
    # MUDANÇA AQUI: Em vez de voltar para 'index', vai para o carrinho
    return redirect('ver_carrinho')

def ver_carrinho(request):
    # Pega os IDs salvos na sessão
    ids_carrinho = request.session.get('carrinho', [])
    
    # Busca os produtos reais no banco
    produtos = Produto.objects.filter(id__in=ids_carrinho)
    
    # === NOVA LÓGICA: CALCULAR TOTAL ===
    # Soma o preço de todos os produtos da lista
    total = sum([produto.preco for produto in produtos])
    
    context = {
        'produtos': produtos,
        'total': total # Enviamos o total para o HTML
    }
    return render(request, 'carrinho.html', context)

def remover_carrinho(request, pk):
    carrinho = request.session.get('carrinho', [])
    
    if pk in carrinho:
        carrinho.remove(pk)
    
    request.session['carrinho'] = carrinho
    return redirect('ver_carrinho')