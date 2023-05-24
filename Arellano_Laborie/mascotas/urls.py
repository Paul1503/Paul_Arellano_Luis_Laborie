from  django.urls import path
from .views import inicio,nosotros,tienda,contacto,buscador

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros/', nosotros, name="nosotros"),
    path('nosotros/tienda', tienda, name='tienda'),
    path('nosotros/tienda/contacto/', contacto, name='contacto'),
    path('nosotros/tienda/contacto/buscador/', buscador, name='buscador'),
]