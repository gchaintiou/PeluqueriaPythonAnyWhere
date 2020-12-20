from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True)
    email = forms.CharField(label="email",required=True)
    asunto = forms.CharField()
    mensaje = forms.CharField(label="Mensaje")