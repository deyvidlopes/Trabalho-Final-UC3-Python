from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(verbose_name="Descrição")
    preco = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Preço")
    # O campo 'imagem' abaixo atende ao requisito de Upload de Imagens (Item 8)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    estoque = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    
    # Relacionamento com Categoria (permite filtrar produtos por categoria depois)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    # Opcional: Relacionamento com quem cadastrou (para controle)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
