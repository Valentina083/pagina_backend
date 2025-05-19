from rest_framework import viewsets
from productos.models import Producto
from productos.serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all()
        categoria_nombre = self.request.query_params.get('categoria', None)
        if categoria_nombre:
            queryset = queryset.filter(categoria__nombre__iexact=categoria_nombre)
        return queryset
