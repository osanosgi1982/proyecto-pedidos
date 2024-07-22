
from winreg import QueryValue
from django.http import HttpResponse
from django.shortcuts import render,redirect
from carro.carro import Carro
from servicios.models import servicios
from .forms import FormularioContacto #cambie en el contacto
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator #paginador
from django.http import HttpResponseForbidden
#para manejar los errores de las urls en el navegador
def custom_error_view(request, exception):
    return render(request, 'custom_error.html', {'message': 'No tienes permiso para acceder a esta página.'})


def home(request):
    carro=Carro(request)
    return render(request,'home.html')

@login_required
def servi(request): #modifique de servicios a servi
    listado=servicios.objects.all()
    paginator=Paginator(listado,1)
    pagina= request.GET.get("page") or 1
    lista=paginator.get_page(pagina)
    pagina_actual=int(pagina)
    paginas=range(1,lista.paginator.num_pages+1)
    return render(request,'servicios.html',{"servicios":lista,"paginas":paginas,"pagina_actual":pagina_actual})

# def tienda(request):
#     return render(request,'tienda.html')

# def blog(request):
#     return render(request,'blog.html')

def contacto(request): #modfique el contacto
    formulario=FormularioContacto()
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde APP gestion de pedidos", 
            "el usuario {} con nombre de la direccion {} escribe el siguiente asunto \n\n <h1> {} </h1> ".format(nombre,email,contenido),
            "",["senaadso058@gmail.com"],reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")
        
    return render(request,'contacto.html',{"miformulario":formulario})


#_________________________________________
from datetime import datetime

def my_view(request):
    # Obtén la hora actual
    current_time = datetime.now().time()
    
    # Define el rango de tiempo en el que la sección del menú debe estar habilitada
    start_time = datetime.strptime('03:00:00', '%H:%M:%S').time()
    end_time = datetime.strptime('04:00:00', '%H:%M:%S').time()
    
    # Verifica si la hora actual está dentro del rango
    if start_time <= current_time <= end_time:
        show_menu_section = False
    else:
        show_menu_section = True

    return render(request, 'base.html', {'show_menu_section': show_menu_section})