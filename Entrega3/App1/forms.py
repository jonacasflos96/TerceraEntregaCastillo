from django import forms

class ProductoFormulario(forms.Form):
    id= forms.IntegerField()
    nombre= forms.CharField()
    paquete= forms.IntegerField()
    
    