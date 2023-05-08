from django.db import models

# Create your models here.
class inicio(models.Model):
    nombre= models.CharField(max_length=40)
class Producto(models.Model):
    nombre= models.CharField(max_length=40)
    paquete= models.IntegerField()
class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
class Información(models.Model):
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    interés= models.CharField(max_length=30)
class Fotos(models.Model):
    nombre= models.CharField(max_length=30)
    fechasesion= models.DateField()
    entregado= models.BooleanField()

























    