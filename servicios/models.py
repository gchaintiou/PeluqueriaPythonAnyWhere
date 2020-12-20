from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servicio(models.Model):    
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class  Meta():
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
    def __str__(self):
        return self.titulo

class Profesional(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profesionales')
    Biografia = models.TextField()
    Formacion = models.TextField()
    activo = models.BooleanField(default=True)
    servicios = models.ManyToManyField(Servicio)
    class  Meta():
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"
    def __str__(self):
        return '%s %s' % (self.usuario.first_name, self.usuario.last_name)

class Trabajo(models.Model):
    Profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    imagenAntes = models.ImageField(upload_to='servicios/trabajos',null=True, blank=True)
    imagenDespues = models.ImageField(upload_to='servicios/trabajos',null=True, blank=True)
    def __str__(self):
        return self.descripcion
