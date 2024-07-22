"""
URL configuration for proyectoweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('',include('proyectowebapp.urls')),
    path('',include('tienda.urls')),
    path('autenticacion/',include('autenticacion.urls')),
    path('carro/',include('carro.urls')),#adicionar url
    path('pedidos/',include('pedidos.urls')),#24 mayo
    # path('', views.home, name="Home"),
    # path('servicios/', views.servicios, name="Servicios"),
    # path('tienda/', views.tienda, name="Tienda"),
    # path('blog/', views.blog, name="Blog"),
    # path('contacto/', views.contacto, name="Contacto"),
]
