from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import ClienteFormulario
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
def ClienteFormulario(request):
     if request.method == 'POST':
        miFormulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            cliente = Cliente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'])
            cliente.save()
            return render(request, "App1/inicio.html")
     else:
        miFormulario = ClienteFormulario('request')
             
     return render(request, "App1/ClienteFormulario.html", {"miFormulario": miFormulario})
