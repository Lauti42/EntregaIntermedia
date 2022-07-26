from django.contrib import admin
from .models import Juegos, Genero, Desarrollador, Plataformas

# Register your models here.

admin.site.register(Juegos)
admin.site.register(Genero)
admin.site.register(Desarrollador)
admin.site.register(Plataformas)