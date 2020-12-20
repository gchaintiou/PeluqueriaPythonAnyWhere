from django.contrib import admin
from .models import Profesional,Servicio,Trabajo


class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

# Register your models here.
admin.site.register(Profesional)
admin.site.register(Servicio,ServicioAdmin)
admin.site.register(Trabajo)
