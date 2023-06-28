from django.urls import path
from .views import inicio, tienda, buscador, contacto, nosotros, administrar, agregarProducto, editarProducto, eliminarProducto, registrar

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
]