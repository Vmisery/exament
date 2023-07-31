from django.http import HttpResponse
from django.template import Template, Context, loader


def PaginaPrincipal(request):
    plantillaExterna = loader.get_template('1.html')
    documento = plantillaExterna.render({})
    return HttpResponse(documento)

def Mision(request):
    plantillaExterna = loader.get_template('2.html')
    documento = plantillaExterna.render({})
    return HttpResponse(documento)

def Galeria(request):
    plantillaExterna = loader.get_template('3.html')
    documento = plantillaExterna.render({})
    return HttpResponse(documento)

def Formulario(request):
    plantillaExterna = loader.get_template('4.html')
    documento = plantillaExterna.render({})
    return HttpResponse(documento)

def Mapa(request):
    plantillaExterna = loader.get_template('5.html')
    documento = plantillaExterna.render({})
    return HttpResponse(documento)