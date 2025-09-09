from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola soy Aguilar desde Django, listo para PythonAnywhere!")
