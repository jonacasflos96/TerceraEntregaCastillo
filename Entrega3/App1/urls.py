from django.urls import path 
from App1 import views

urlpatterns=[

    path('inicio', views.inicio, name='inicio'),
    path('Producto', views.Producto, name='Producto'),
    path('Cliente', views.Cliente, name='Cliente'),
    path('Información', views.Información, name='Información'),
    path('Fotos', views.Fotos, name='Fotos'),
    path('ProductoFormulario', views.ProductoFormulario, name="ProductoFormulario")
    
]