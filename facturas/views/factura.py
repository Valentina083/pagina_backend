from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from facturas.models import Factura, DetalleFactura
from usuarios.models import Usuario
from facturas.serializers import FacturaSerializer, DetalleFacturaSerializer
from productos.models import Producto


class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializer

    def get(self, request, factura_id):
        try:
            factura = Factura.objects.get(id=factura_id)
        except Factura.DoesNotExist:
            return Response({"error": "Factura no encontrada"}, status=404)

        detalle = factura.detalle.all()
        serializer = DetalleFacturaSerializer(detalle, many=True)
        return Response(serializer.data)


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

    def create(self, request):
        print("Entré a la vista create")
        # Recibe datos del usuario desde el frontend
        nombre = request.data.get("nombre")
        correo = request.data.get("correo")
        telefono = request.data.get("telefono")
        direccion = request.data.get("direccion")
        productos = request.data.get("carrito")  # Lista de productos
        print("Productos recibidos del frontend:", productos)

        if not correo or not nombre:
            return Response({"error": "El nombre y correo son obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

        if not productos or not isinstance(productos, list):
            return Response({"error": "No se recibieron productos válidos."}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar o crear el usuario
        usuario, creado = Usuario.objects.get_or_create(
            correo=correo,
            defaults={
                "nombre": nombre,
                "telefono": telefono,
                "direccion": direccion,
            }
        )

        # Calcular total de la compra
        total = sum(float(item["precio"]) * item["cantidad"] for item in productos)

        # Crear factura
        factura = Factura.objects.create(
            cliente=usuario,
            total=total,
            fecha=now()
        )

        # Crear detalles de factura
        for item in productos:
            try:
                producto = Producto.objects.get(id=item["id"])
            except Producto.DoesNotExist:
                print("Producto con ID", item["id"], "no existe")

            print("Creando detalle:", producto.nombre, item["cantidad"], item["precio"])

            DetalleFactura.objects.create(
                factura=factura,
                producto=producto,
                cantidad=item["cantidad"],
                precio=item["precio"]
            )
        factura = Factura.objects.prefetch_related('detalles__producto').get(id=factura.id)
        serializer = FacturaSerializer(factura)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
