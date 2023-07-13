from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID categoría")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre categoría")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, verbose_name="Código")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    descripcion = models.CharField(max_length=35, verbose_name="Descripción")
    imagen = models.ImageField(upload_to="productos", null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return self.nombre
    
class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now)
    estadoOpciones=(
        ('procesandoPedido', 'Procesando Pedido' ),
        ('enviado', 'Enviado'),
        ('enCamino', 'En camino'),
        ('entregado', 'Entregado'),
    )
    estado = models.CharField(max_length=25, choices=estadoOpciones, default='procesandoPedido')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
    
    def __str__(self):
        return str(self.id_boleta)

class DetalleBoleta(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_boleta = models.ForeignKey(Boleta, blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)
