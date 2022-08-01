from rest_framework import serializers

from .models import Habitante, Ciudad
class HabitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitante
        fields = ['id', 'cedula', 'nombres', 'apellidos', 'direccion', 'telefono', 'ciudad']


class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['id', 'ciudad']