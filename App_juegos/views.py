from django.shortcuts import render

from .forms import FormularioDesarrollador, FormularioGenero, FormularioJuegos, FormularioPlataformas

from .models import Desarrollador, Genero, Juegos, Plataformas

from django.http import HttpResponse
from django.template import Template, Context, loader


# Create your views here.

#           VISTAS
def inicio(self):

    return render(self, "inicio.html")


def juegos(self):

    # juegos = Juegos.objects.all()

    # return render(self, "juegos.html", {"juegos": juegos})

    plantilla = loader.get_template("juegos.html")

    documento = plantilla.render({"juegos": Juegos.objects.all()})

    return HttpResponse(documento)

def generos(self):

    generos = Genero.objects.all()

    return render(self, "generos.html", {"plataformas": generos})

def desarrolladores(self):

    desarrolladores = Desarrollador.objects.all()

    return render(self, "desarrolladores.html", {"plataformas": desarrolladores})

def plataformas(self):

    familiares = Plataformas.objects.all()

    return render(self, "plataformas.html", {"plataformas": familiares})

#           FORMULARIOS

def formulariojuegos(request):

    if request.method == 'POST':

        juegos = Juegos( nombre=request.POST['nombre'], anodecreacion=request.POST['anodecreacion'], desarrollador=request.POST['desarrollador'], genero=request.POST['genero'])
        
        juegos.save()

        return render(request, 'juegos.html')

    return render(request, "formulario-juegos.html")

    # plantilla = loader.get_template("formulario-juegos.html")

    # documento = plantilla.render({"juegos": Juegos.objects.all()})

    # return HttpResponse(documento)


def formulariogeneros(request):

    if request.method == 'POST':

        miformulario = FormularioGenero(request.POST)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            estudio = Genero( nombre=data['nombre'])
        
            estudio.save()

            return render(request, 'generos.html')

    else:
        
        miformulario = FormularioGenero() 

    return render(request, 'formulario-genero.html', {'miformulario': miformulario})

def formulariodesarrolladores(request):

    if request.method == 'POST':

        miformulario = FormularioDesarrollador(request.POST)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            estudio = Desarrollador( nombre=data['nombre'], pais=data['pais'])
        
            estudio.save()

            return render(request, 'desarrolladores.html')

    else:
        
        miformulario = FormularioDesarrollador() 

    return render(request, 'formulario-desarrollador.html', {'miformulario': miformulario})

def formularioplataformas(request):

    if request.method == 'POST':

        juegos = Plataformas( nombre=request.POST['nombre'], juegos=request.POST['juegos'], link=request.POST['link'])
        
        juegos.save()

        return render(request, 'plataformas.html')

    return render(request, "formulario-plataforma.html")