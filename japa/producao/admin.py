from django.contrib import admin
from .models import Estoque, Ingrediente, ProdutoFinal, Temperatura
# Register your models here.
admin.site.register(Estoque)
admin.site.register(Ingrediente)
admin.site.register(ProdutoFinal)
admin.site.register(Temperatura)