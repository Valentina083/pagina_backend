from django.db import models
from django.utils.timezone import now
from productos.models import Producto
from usuarios.models import Usuario


class Factura(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(default=now)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    productos = models.ManyToManyField(Producto, through='DetalleFactura')

    def __str__(self):
        return f"Factura #{self.id} - Cliente: {self.cliente}"


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
