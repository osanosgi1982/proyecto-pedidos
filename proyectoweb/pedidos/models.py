
#from xml.parsers.expat import model
from django.db import models
from django.db.models import F,Sum,FloatField

from django.contrib.auth import get_user_model # devuelve el usuario actual
from tienda.models import Producto
# Create your models here.

User=get_user_model()
class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.cantidad} unidades {self.producto_id.nombre}")

    def precio_unitario(self):
        return self.producto.precio
    
    def sub_total(self):
        return self.producto.precio * self.cantidad

    class Meta:
        db_table='lineapedidos'
        verbose_name='linea pedido'
        verbose_name_plural='lineas pedidos'
        ordering=['id']

