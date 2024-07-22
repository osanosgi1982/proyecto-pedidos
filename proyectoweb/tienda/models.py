from datetime import datetime
from distutils.command.upload import upload
from mailbox import NoSuchMailboxError
from tabnanny import verbose
from turtle import mode
from django.db import models

# Create your models here.
class CategoriaPro(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoria"
        verbose_name_plural ="categorias"
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    cateogrias=models.ForeignKey(CategoriaPro, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda")
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="producto"
        verbose_name_plural ="productos"

