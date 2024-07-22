from dataclasses import fields
from django.shortcuts import render,redirect
from django.views.generic import View #para cargar las vistas genericas
from django.contrib import messages #para los mensajes de error del formulario
from django import forms #29de mayo
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm #para crear el formulario para el registro de usuarios
from django.contrib.auth import login,logout,authenticate #sirve para generar el agua
from django.contrib.auth.models import User
from django.contrib import messages

#29 de mayo
class UserCreationFormWithEmail(UserCreationForm):
  email= forms.EmailField(required=True,help_text="Ingrese un email valido")

  class Meta:
    model=User
    fields=("username","email","password1","password2")

  

# Create your views here.
#esto se comentara mas adelante
#def autenticacion(request):
  #  return render(request,"registro/registro.html")

class VRegistro(View):
    def get(self,request):
        form=UserCreationForm
        return render(request,"registro/registro.html",{"form":form})

    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
          usuario=form.save()#guardar lo llenado en el formulario
          #messages.success(request,"Usuario Registrado")
          login(request,usuario)#sirve para generar el login en la tabla auth
          messages.success(request,"Usuario Registrado")
          return redirect('Home')
        else:
          for msg in form.error_messages:
            messages.error(request,form.error_messages[msg])
        return render(request,"registro/registro.html",{"form":form})

def cerrar_sesion(request):
  logout(request)
  return redirect('Home')

def logear(request):
  if request.method=="POST":
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      nombre_usuario=form.cleaned_data.get("username")
      contrasena=form.cleaned_data.get("password")
      usuario=authenticate(username=nombre_usuario,password=contrasena)
      if usuario is not None:
        login(request,usuario)
        return redirect('Home')
      else:
        messages.error(request,"Usuario no logeado")
    else:
      messages.error(request,"Informacion Incorrecta")
  form=AuthenticationForm()
  return render(request,"login/login.html",{"form":form})

