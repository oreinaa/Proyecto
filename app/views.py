from django.shortcuts import render, redirect
from .models import Categoria, Cliente, Marca, Producto
from .forms import ClienteForm, CategoriaForm, MarcaForm, ProductoForm


def home(request):
    clientes = Cliente.objects.all
    context = {"clientes": clientes}
    return render(request, 'home.html', context)

def agregar(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = ClienteForm()
    
    context= {'form': form}
    return render(request, 'agregar.html', context)

def eliminar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('home')

def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid:
            form.save()
            return redirect('home')
        
    else:
        form = ClienteForm(instance=cliente)

    context= {'form': form}
    return render(request, 'editar.html', context)


#Categoria

def listaCat(request):
    categorias = Categoria.objects.all
    context = {'categorias': categorias}
    return render(request, 'categoria/listadocat.html', context)

def agregar_Cat(request):
    if request.method == 'POST':
        f = CategoriaForm(request.POST)
        if f.is_valid():
            cate = Categoria(nombre=f.cleaned_data['nombre'],)
            cate.save(request)
            return redirect('listadocat')
    else:
        f = CategoriaForm()

    context= {'form':f}
    return render(request, 'categoria/agregarcat.html', context)

'''def agregar_Cat(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('listadocat')
    else:
        form = CategoriaForm()

    context= {'form':form}
    return render(request, 'categoria/agregarcat.html', context)'''

def eliminar_Cat(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('listadocat')

def editar_Cat(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == 'POST':
        f = CategoriaForm(request.POST, instance=categoria)
        if f.is_valid():
            f.save()
            return redirect ('listadocat')
    else:
        f = CategoriaForm(instance=categoria)
    
    context = {'form': f}
    return render(request, 'categoria/editar.html', context)

#Marca

def listaMarca(request):
    marcas = Marca.objects.all
    context = {'marcas': marcas}
    return render(request, 'marca/listadomarca.html', context)

def agregar_Marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('listadomarca')
    else:
        form = MarcaForm()

    context= {'form':form}
    return render(request, 'marca/agregarmarca.html', context)

def eliminar_Marca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    return redirect('listadomarca')

def editar_Marca(request, id):
    marca = Marca.objects.get(id=id)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('listadomarca')
    else:
        form = MarcaForm(instance=marca)
    
    context = {'form': form}
    return render(request, 'marca/editarmarca.html', context)

#Producto

def listaProd(request):
    productos = Producto.objects.all
    context = {'productos': productos}
    return render(request, 'producto/listadoprod.html', context)

def agregar_Producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('listadoprod')
    else:
        form = ProductoForm()

    context= {'form':form}
    return render(request, 'producto/agregar.html', context)

