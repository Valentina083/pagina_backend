from django.db import models
from productos.models import Producto


class Carrito(models.Model):
    session_id = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    imagen = models.URLField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.session_id} - {self.producto.nombre} ({self.cantidad})"
