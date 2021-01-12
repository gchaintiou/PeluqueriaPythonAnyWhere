from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('servicios/',views.servicios,name="Servicios"),
    path('profesionales/',views.profesionales,name="Profesionales"),
    path('servicios/trabajos/<int:idServicio>/',views.trabajos,name="Trabajos"),
    path('profesional/servicio/trabajos/<int:idProfesional>/<int:idServicio>',views.ProfServicioTrabajos, name="ProfServicioTrabajos"),
]
urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
