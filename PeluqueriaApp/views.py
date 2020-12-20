from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'PeluqueriaApp/home.htm')


def tienda(request):
    return render(request, 'PeluqueriaApp/tienda.htm')
