from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)

class EntregablesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
               