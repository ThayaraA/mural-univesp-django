from django.contrib import admin
from .models import Duvida

@admin.register(Duvida)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'criado', 'modificado', 'ativo')

