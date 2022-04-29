from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('agregar/', views.agregar, name="agregar"),
    path('eliminar/<id>/',views.eliminar, name='eliminar'),
    path('editar/<id>/',views.editar, name='editar'),
    path('listadocat/', views.listaCat, name='listadocat'),
    path('agregarcat/', views.agregar_Cat, name='agregarcat'),
    path('eliminarcat/<id>/',views.eliminar_Cat, name='eliminarcat'),
    path('editarcat/<id>/',views.editar_Cat, name='editarcat'),
    path('listadomarca/', views.listaMarca, name='listadomarca'),
    path('agregarmarca/', views.agregar_Marca, name='agregarmarca'),
    path('eliminarmarca/<id>/',views.eliminar_Marca, name='eliminarmarca'),
    path('editarmarca/<id>/',views.editar_Marca, name='editarmarca'),
    path('listadoprod/', views.listaProd, name='listadoprod'),
    path('agregarproducto/', views.agregar_Producto, name='agregarprod'),

]