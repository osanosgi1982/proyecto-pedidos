from django.contrib import admin
from tienda.models import Producto,CategoriaPro
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(CategoriaPro, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)