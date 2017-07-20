from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        email = form.cleaned_data['email']
        obj = Registrado.objects.create(email=email, nombre=nombre)
    context = {
        "form": form,
    }
    return render(request, "inicio.html", context)
