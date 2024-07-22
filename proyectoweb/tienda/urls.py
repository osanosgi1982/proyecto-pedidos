from django.urls import path

from . import views
from tienda.views import ReporteAutorExcel, tienda

Appname=tienda
urlpatterns = [
    
    path('tienda', views.tienda, name="Tienda"),
    # path('blog/', views.blog, name="Blog"),
    #modifique 11 de junio
    path('listado', views.listado, name="listado"),
    path('reporte', views.ReporteAutorExcel.as_view(), name="reporte"),
    path('listarproductos',views.ListaProductoPdf.as_view(),name='productos'),
     path('api', views.api, name="api"),

   
]

