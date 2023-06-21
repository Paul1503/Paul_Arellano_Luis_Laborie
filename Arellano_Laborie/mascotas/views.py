from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, RegistroUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def tienda(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'tienda.html',datos)

def buscador(request):
    return render(request, 'buscador.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')

@login_required
def administrar(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    return render(request, 'administrar.html', datos)

@login_required
def agregarProducto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('administrar')
        else:
            datos["form"] = formulario
    return render(request, 'agregarProducto.html', datos)

@login_required
def editarProducto(request, id):
    productoeditado=Producto.objects.get(codigo=id)
    datos ={
        'form':ProductoForm(instance=productoeditado)
    }
    if request.method=="POST":
        formulario = ProductoForm(data=request.POST, instance=productoeditado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('administrar')
    return render(request, 'editarProducto.html', datos)

@login_required
def eliminarProducto(request, id): 
    productoEliminado = Producto.objects.get(codigo=id)
    productoEliminado.delete()
    return redirect ('administrar')

def registrar(request):
    data={                   
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('inicio') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)