from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
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

    return render(request, "base.html", context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data['email']
        form_mensaje = form.cleaned_data['mensaje']
        form_nombre = form.cleaned_data['nombre']

        asunto = 'Prueba de email con Django'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, 'joseloarca97@icloud.com']
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        # send_mail(asunto,
        #           email_mensaje,
        #           email_from,
        #           email_to,
        #           fail_silently=False)

    context = {
        "form": form,
    }

    return render(request, "forms.html", context)
