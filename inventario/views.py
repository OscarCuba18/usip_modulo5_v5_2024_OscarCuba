from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria


def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de hoy")

def categorias(request):
    filtro_nombre = request.GET.get("nombre")
    print(filtro_nombre)
    items = Categoria.objects.all()
    return render(request, "categorias.html", {"categorias": items})

def filtrar_categorias(request):
    nombre_filtro = request.GET.get('nombre', None)
    print(nombre_filtro)
    if nombre_filtro:
        categorias = Categoria.objects.filter(nombre__icontains=nombre_filtro)
    else:
        categorias = Categoria.objects.all()
    return render(request, 'categorias_list.html', {'categorias': categorias})
