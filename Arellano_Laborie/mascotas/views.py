from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def tienda(request):
    return render(request, 'tienda.html')

def contacto(request):
    return render(request, 'contacto.html')

def buscador(request):
    return render(request, 'buscador.html')