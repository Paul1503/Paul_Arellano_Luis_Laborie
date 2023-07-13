from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio" ),
    path('tienda/', tienda, name="tienda"),
    path('buscador/', buscador, name="buscador"),
    path('contacto/', contacto, name="contacto"),
    path('nosotros/', nosotros, name="nosotros"),
    path('administrar/', administrar, name="administrar"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('editarProducto/<id>/', editarProducto, name="editarProducto"),
    path('eliminarProducto/<id>/', eliminarProducto, name="eliminarProducto"),
    path('registrar/' , registrar, name="registrar"),
    path('carrito/' , carrito, name="carrito"),
    path('generarBoleta/', generarBoleta,name="generarBoleta"),

    path('agregar/<id>/', agregar_producto, name="agregar"),
    path('eliminar/<id>/', eliminar_producto, name="eliminar"),
    path('restar/<id>/', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]