from rest_framework import serializers
from productos.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True)
    nombre_categoria = serializers.StringRelatedField(source='categoria')

    class Meta:
        model = Producto
        fields = '__all__'
