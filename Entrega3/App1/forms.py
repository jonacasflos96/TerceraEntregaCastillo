from django import forms
 
class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    paquete = forms.IntegerField()
class ClienteFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()