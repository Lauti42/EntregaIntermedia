from django import forms

class FormularioDesarrollador(forms.Form):
    
    nombre = forms.CharField()
    pais = forms.CharField()

class FormularioGenero(forms.Form):
    
    nombre = forms.CharField()

class FormularioJuegos(forms.Form):
    
    nombre = forms.CharField()
    año_de_creacción = forms.IntegerField()
    desarrollador = forms.CharField()
    genero = forms.CharField()    

class FormularioPlataformas(forms.Form):
    nombre = forms.CharField()
    juegos = forms.CharField()
    link = forms.CharField()