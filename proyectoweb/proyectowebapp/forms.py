import email
from django import forms
#29 de mayo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

#29 de mayo
class UserCreationFormWithEmail(UserCreationForm):
  email= forms.EmailField(required=True,help_text="Ingrese un email valido")

  class Meta:
    model=User
    fields=("username","email","password1","password2")

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)
    email=forms.EmailField(label="Email",required=True)
    contenido=forms.CharField(label="Contenido",widget=(forms.Textarea),required=True)