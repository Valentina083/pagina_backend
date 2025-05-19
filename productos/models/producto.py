from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
