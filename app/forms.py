from django import forms
from .models import Cliente, Categoria, Producto, Marca

class ClienteForm(forms.ModelForm):

    class Meta:
        model= Cliente
        fields = ['nombre', 'apellido', 'telefono']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model= Categoria
        fields = ['nombre']

class MarcaForm(forms.ModelForm):

    class Meta:
        model= Marca
        fields = ['nombre']

class ProductoForm(forms.ModelForm):

    class Meta:
        model= Producto
        fields = ['nombre', 'precio', 'categoria','marca']