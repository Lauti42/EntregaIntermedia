from django.db import models

# Create your models here.



class Desarrollador(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.pais}'

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre}'

class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    anodecreacion = models.IntegerField()
    desarrollador = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.anodecreacion}) - {self.genero} - {self.desarrollador}'

class Plataformas(models.Model):
    nombre = models.CharField(max_length=50)
    juegos = models.CharField(max_length=50)
    link = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.juegos}) - {self.link}'