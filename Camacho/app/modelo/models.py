from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
class Producto(models.Model):
	codigo = models.CharField('codigo',max_length= 10)
	nombre = models.CharField('nombre',max_length = 25)
	categoria = models.CharField('categoria',max_length = 25)
	precio = models.CharField(max_length = 25)
	marca = models.CharField(max_length= 10)
	descripcion = models.TextField(default= 'Descripcion')
