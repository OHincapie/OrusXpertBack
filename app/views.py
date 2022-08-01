from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Habitante, Ciudad
from .serializers import CiudadSerializer, HabitanteSerializer, Ciudad

# Create your views here.

class CiudadesView(APIView):

    def get(self, request, format=None):
        ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudades, many=True)
        if len(ciudades) > 0:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CiudadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            ciudad = Ciudad.objects.get(id = request.data['id'])
        except Ciudad.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CiudadSerializer(ciudad, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
  
    def delete(self, request, pk=None):
        try:
            ciudad = Ciudad.objects.get(id = request.data['id'])
        except Ciudad.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ciudad.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class HabtantesView(APIView):
    
    def get(self, request, format=None):
        habitantes = Habitante.objects.all()
        serializer = HabitanteSerializer(habitantes, many=True)
        if len(habitantes) > 0:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = HabitanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            habitante = Habitante.objects.get(id = request.data['id'])
        except Habitante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = HabitanteSerializer(habitante, data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
  
    def delete(self, request, pk=None):
        try:
            habitante = Habitante.objects.get(id = request.data['id'])
        except Habitante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        habitante.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getCityById(request, idCiudad):
    ciudad = Ciudad.objects.get(id = idCiudad)
    serializer = CiudadSerializer(ciudad)
    if ciudad :
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
