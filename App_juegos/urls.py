
from django.urls import path

from .views import desarrolladores, formulariodesarrolladores, formulariogeneros, formulariojuegos, formularioplataformas, generos, inicio, juegos, plataformas

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('juegos/', juegos, name="Juegos"),
    path('generos/', generos, name="Generos"),
    path('desarrolladores/', desarrolladores, name="Desarrolladores"),
    path('plataformas/', plataformas, name="Plataformas"),
    path('formulario-juegos/', formulariojuegos, name="formulariojuegos"),
    path('formulario-genero/', formulariogeneros, name="formulariogenero"),
    path('formulario-desarrollador/', formulariodesarrolladores, name="formulariodesarrollador"),
    path('formulario-plataforma/', formularioplataformas, name="formularioplataforma"),
]
