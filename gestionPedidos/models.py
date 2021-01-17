from django.db import models


class Clientes (models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)


class Articulos (models.Model):
    nombre = models.CharField(max_length=45)
    seccion = models.CharField(max_length=45)
    precio = models.IntegerField()


class Pedidos (models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
