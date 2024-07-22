from django.urls import path
#from . import views #comentar
from .views import VRegistro,cerrar_sesion,logear
urlpatterns=[
   # path('', views.autenticacion, name="Autenticacion"),#comentar
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
    


]