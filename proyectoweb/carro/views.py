from django.shortcuts import render

from tienda.views import tienda
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect
# Create your views here.

def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")
    #carro.agregar(producto=producto)
    #return redirect("Tienda")

def eliminar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request,producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")