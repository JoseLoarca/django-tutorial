from django import forms

from .models import Registrado


class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
#       Mis validaciones irian aca.
        return nombre


class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
