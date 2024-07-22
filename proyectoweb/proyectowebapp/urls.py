from django.urls import path,include

from proyectowebapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler403

from proyectowebapp.views import custom_error_view

urlpatterns = [
    path('', views.home, name="Home"),
    path('servicios/', views.servi, name="Servicios"),#modifique servicios por servi
    # path('tienda/', views.tienda, name="Tienda"),
    # path('blog/', views.blog, name="Blog"),
    path('contacto/', views.contacto, name="Contacto"),
    path('tienda/', include(('tienda.urls', 'tienda'), namespace='tienda')),
    
]
handler403=custom_error_view
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
