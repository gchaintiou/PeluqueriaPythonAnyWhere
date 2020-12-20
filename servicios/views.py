from django.shortcuts import render,HttpResponse
from .models import Profesional,Servicio,Trabajo

# Create your views here.
def profesionales(request):
    profesionales = Profesional.objects.all()
    servicios = Servicio.objects.all()
    return render(request, 'servicios/profesionales.html', {"profesionales": profesionales, "servicios":servicios})

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.html', {"servicios": servicios})

def trabajos(request,idServicio):
    servicio = Servicio.objects.get(id=idServicio)
    trabajos = Trabajo.objects.filter(servicio_id = idServicio)
    return render(request,'servicios/trabajos.html',{'servicio':servicio,'trabajos':trabajos})