from django.shortcuts import render
from .forms import FormularioContacto
from django.core.mail import send_mail

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    return render(request, 'contacto/contacto.html',{"miFormulario":formulario_contacto})
    
# def contacto(request):
#     if request.method = "POST":
#         miFormulario = FormularioContacto(request.POST) #Obtiene los datos del post
#         if miFormulario.is_valid():
#             infForm = miFormulario.cleaned_data
#             send_mail(infForm['asunto'])

#     formulario_contacto = FormularioContacto()
#     return render(request, 'contacto/contacto.html',{"miFormulario":formulario_contacto})
