from django.contrib import admin
from .models import Categoria, Produto, ImagemProduto

# Permite adicionar imagens extras DENTRO da tela do Produto
class ImagemProdutoInline(admin.TabularInline):
    model = ImagemProduto
    extra = 1 # Quantos campos vazios aparecem

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria', 'ativo')
    list_filter = ('ativo', 'categoria')
    search_fields = ('nome',)
    # Adiciona a área de fotos extras no final do cadastro
    inlines = [ImagemProdutoInline]

admin.site.register(Categoria)