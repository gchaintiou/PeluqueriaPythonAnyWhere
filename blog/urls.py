from django.urls import path
from . import views

urlpatterns = [
    path('blog/',views.blog,name="Blog"),
    path('blog/categoria/<int:categoria_id>/',views.categoria,name="Categoria")
]
