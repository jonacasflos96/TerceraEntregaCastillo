from django.shortcuts import render
import requests
from App1.models import Producto
from django.http import HttpResponse
from App1.forms import ProductoFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def Producto(request):
    return render(request, 'App1/producto.html')
def Cliente(request):
    return render(request, 'App1/cliente.html')
def Información(request):
   return render(request, 'App1/informacion.html')
def Fotos(request):
    return render(request, 'App1/fotos.html')

def ProductoFormulario(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(int(informacion['id']),str(informacion['nombre']),int(informacion['paquete']))
            producto.save()
            return render(request, "App1/inicio.html")
    else:
            miFormulario = ProductoFormulario()
 
    return render(request, "App1/ProductoFormulario.html", {"miFormulario": miFormulario})
            
            