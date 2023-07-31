from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    tecnica = models.CharField(max_length=30)