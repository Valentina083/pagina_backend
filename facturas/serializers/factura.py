from rest_framework import serializers
from facturas.models import Factura, DetalleFactura


class DetalleFacturaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = DetalleFactura
        fields = ['producto_nombre', 'cantidad', 'precio', 'subtotal']

    def get_subtotal(self, obj):
        return float(obj.cantidad) * float(obj.precio)


class FacturaSerializer(serializers.ModelSerializer):
    detalles = DetalleFacturaSerializer(many=True, read_only=True)
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)

    class Meta:
        model = Factura
        fields = ['id', 'cliente_nombre', 'fecha', 'total', 'detalles']
