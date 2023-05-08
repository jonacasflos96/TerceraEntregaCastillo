#Pasos para construir el proyecto.
#1 Entras a tu carpeta y escribes python -m django startproject Proyecto1 esto lo que hará es crear todas las carpetas
#además, tenemos que insertar el siguiente comando python manage.py migrate 
#2 primero tienes que crear las funciones en views, después importamos la función en urls y creas el path para el link
#3 Crear una plantilla. Cuando quieres jalar algo de la plantilla tienes que crear una función con una instancia y una ruta señalando al template
#4 ponerle un cargador para que te lea la plantilla más facil y cambiar la función
#5 python manage.py startapp <nombre de la aplicación>


from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader 


def probandoTemplate(self):
    nomb='David'
    ap='BU'
    dia = datetime.datetime.now()
    notas= [1,2,3,4,5]
    diccionario={'nombre':nomb, 'apellido':ap,'fecha':dia,'notas':notas}
    #miHtml = open("C:/Users/Windows/Desktop/Curso-Python-Backend/Clase 18/Proyecto1/Proyecto1/plantillas/template1.html")
    #plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    #miHtml.close() #Cerramos el archivo
    #miContexto = Context(diccionario) #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    #documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    plantilla= loader.get_template('template1.html')
    documento = plantilla.render(diccionario) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)
  
    
