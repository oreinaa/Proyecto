from django.contrib import admin
from .models import Cliente, Marca, Producto, Categoria

admin.site.register(Cliente)
admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto)

