from django.db import models

# Create your models here.
class Ciudad(models.Model):
    ciudades = (
        ('Bogotá', 'Bogotá'),
        ('Armenia', 'Armenia'),
        ('Barranquilla', 'Barranquilla'),
        ('Bucaramanga', 'Bucaramanga'),
        ('Cali', 'Cali'),
        ('Cartagena', 'Cartagena'),
        ('Cucuta', 'Cucuta'),
        ('Ibague', 'Ibague'),
        ('Manizales', 'Manizales'),
        ('Medellin', 'Medellin'),
        ('Pereira', 'Pereira'),
        ('Santa Marta', 'Santa Marta'),
        ('Villavicencio', 'Villavicencio')
    )
    ciudad = models.CharField(max_length = 50, default = 'Bogotá', unique = True)
 
    def __str__(self) -> str:
        return '{}'.format(self.ciudad)


    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'ciudad'


class Habitante(models.Model):
    cedula = models.PositiveBigIntegerField(unique = True)
    nombres = models.CharField(max_length = 255)
    apellidos = models.CharField(max_length = 255)
    direccion = models.CharField(max_length = 255)
    telefono = models.PositiveBigIntegerField()
    ciudad = models.ForeignKey(Ciudad, related_name='ciudad_id', on_delete = models.CASCADE)
 
    def __str__(self) -> str:
        return '{} | {} {} | {}'.format(self.cedula, self.nombres, self.apellidos, self.ciudad)


    class Meta:
        verbose_name = 'Habitante'
        verbose_name_plural = 'Habitantes'
        db_table = 'habitantes'