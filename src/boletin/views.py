from django.shortcuts import render

from .forms import RegForm, RegModelForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Formulario Registro"
    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
        "titulo": titulo,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.nombre:
            user, proveedor = instance.email.split("@")
            instance.nombre = user
        instance.save()
        print(instance)
        print(instance.timestamp)

    context = {
        "titulo": "Gracias por registrarte!",
    }

    return render(request, "inicio.html", context)
