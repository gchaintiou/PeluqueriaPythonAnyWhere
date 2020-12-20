from django.urls import path
from PeluqueriaApp import views


urlpatterns = [
    path('',views.home,name="Home"),
    path('tienda/',views.tienda,name="Tienda"),
]
