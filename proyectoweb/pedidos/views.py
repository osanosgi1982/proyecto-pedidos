import logging
from multiprocessing import Value
from urllib.request import Request
from django.shortcuts import render,redirect
from pedidos.models import Pedido,LineaPedido
from carro.carro import Carro
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string #24mayo
from django.utils.html import strip_tags
from django.core.mail import send_mail

from tienda.models import Producto
# Create your views here.
@login_required()
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        producto_id=key
        cantidad=value["cantidad"]
        producto=Producto.objects.get(id=producto_id)
        lineas_pedido.append(LineaPedido(
            producto=producto,
            cantidad=cantidad,
            user=request.user,
            pedido=pedido,
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username, #corregir
        emailusuario=request.user.email, #corregir

    )

    messages.success(request, "El pedido se ha hecho correctamente")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario")
    })
    mensaje_texto=strip_tags(mensaje) #strip tags es para limpiar el mensaje de html
    from_email="senaadso058@gmail.com"
    #to=kwargs.get("emailusuario")
    to="oospinag@sena.edu.co"

    send_mail(asunto,mensaje_texto,from_email,[to],html_message=mensaje)

