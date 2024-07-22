from django.contrib import admin
from .models import servicios

# Register your models here.
class serviciosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(servicios, serviciosAdmin)