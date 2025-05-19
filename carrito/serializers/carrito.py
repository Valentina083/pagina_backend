from rest_framework import serializers
from carrito.models import Carrito


class CarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carrito
        fields = '__all__'
