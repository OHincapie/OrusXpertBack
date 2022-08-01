from django.core.management.base import BaseCommand
from ...models import Ciudad

class Command (BaseCommand):
    help = 'import booms'
    citys= [
         'Bogotá',
         'Armenia',
         'Barranquilla',
         'Bucaramanga',
         'Cali',
         'Cartagena',
         'Cucuta',
         'Ibague',
         'Manizales',
         'Medellin',
         'Pereira',
         'Santa Marta',
         'Villavicencio'
    ]

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for city in self.citys:
            model = Ciudad(ciudad = city)
            model.save()
