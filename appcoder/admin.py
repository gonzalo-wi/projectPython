from django.contrib import admin
from .models import *


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields=('nombre','id')
    list_filter=('nombre',)
    list_per_page=20
    list_display=('id','nombre','comision')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    search_fields=('nombre','apellido','id')
    list_filter=('id',)
    list_per_page=20
    list_display=('id','nombre','apellido','email')

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    search_fields=('nombre','apellido','profesion','id')
    list_filter=('id','apellido')
    list_per_page=20
    list_display=('id','nombre','apellido','email','profesion')

@admin.register(Entregable)
class EntregableAdmin(admin.ModelAdmin):
    search_fields=('nombre','id')
    list_filter=('entregado',)
    list_per_page=20
    list_display=('id','nombre','fecha_de_entrega','entregado')    