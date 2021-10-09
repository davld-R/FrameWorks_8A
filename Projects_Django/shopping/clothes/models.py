from django.db import models
from django.db.models.fields import CharField

class Marca(models.Model) :
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    tipo_marca = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)
    #Aqui van las llaves foraneas

class Sucursal(models.Model) :
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, default= "")

class Cliente(models.Model) :
    nombre = models.CharField(max_length=100)