from django.shortcuts import render, redirect
from .models import Producto, Boleta, DetalleBoleta
from .forms import ProductoForm, RegistroUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from mascotas.compras import Carrito

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

@login_required
def tienda(request):
    productos = Producto.objects.all()
    pagina = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos,10)
        productos = paginator.page(pagina)
    except:
        raise Http404
    datos = {
        'productos' : productos,
        'paginator' : paginator
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


def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.agregar(producto=producto)
    return redirect(request.META['HTTP_REFERER'])

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = Producto.objects.get(codigo=id)
    carrito_compra.restar(producto=producto)
    return render(request, 'carrito.html')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return render(request,'carrito.html')

def carrito(request):
    return render(request, 'carrito.html')



def generarBoleta(request):
    productos = []
    precioTotal = 0

    for key, value in request.session['carrito'].items():
        producto = Producto.objects.get(codigo=value['producto_id'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])

        if cant > producto.stock:
            mensaje_error = f"No hay suficiente stock disponible para el producto {producto.nombre}. Stock actual: {producto.stock}"
            return render(request, 'carrito.html', {'mensaje_error': mensaje_error})

        precioTotal += subtotal
        producto.stock -= cant
        producto.save()

        detalle = DetalleBoleta(id_producto=producto, cantidad=cant, subtotal=subtotal)
        productos.append(detalle)

    impuesto = round(precioTotal * 0.19)
    envio = 3990
    precioTotal += impuesto + envio

    boleta = Boleta(total=precioTotal, usuario=request.user)
    boleta.save()
    boleta.estado = 'procesandoPedido'
    boleta.save()

    for detalle in productos:
        detalle.id_boleta = boleta
        detalle.save()

    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'impuesto': impuesto,
        'envio': envio,
        'total': boleta.total
    }

    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()

    return render(request, 'carritoDetalle.html', datos)


