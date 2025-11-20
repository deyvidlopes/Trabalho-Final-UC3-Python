from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'categoria', 'ativo')
    list_filter = ('ativo', 'categoria') # Cria filtro lateral no admin (Item 8)
    search_fields = ('nome',) # Cria barra de busca

admin.site.register(Categoria)