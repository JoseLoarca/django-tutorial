from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]
    
    def clean_email(self):
        email = self.cleaned_data['email']
        #email_base, proveedor = email.split("@")
        #dominio, extension = proveedor.split(".")
        #if not extension == "edu":
            #raise forms.ValidationError("Por favor, utiliza un email con la extensión .edu ")
        return email
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        #Mis validaciones irian aca.
        return nombre

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
