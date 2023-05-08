from django.shortcuts import render
from App1.models import Producto, Cliente, Información, Fotos, inicio
from django.http import HttpResponse
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
