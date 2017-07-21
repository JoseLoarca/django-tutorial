from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Formulario Registro"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)
    form = RegForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        obj = Registrado.objects.create(email=email, nombre=nombre)
    context = {
        "titulo":titulo,
        "form": form,
    }
    return render(request, "inicio.html", context)
