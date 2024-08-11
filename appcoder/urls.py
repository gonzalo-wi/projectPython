from django.urls import path
from appcoder.views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cursos/', CursoListView.as_view(), name="cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('profesores/', profesores, name="profesores"),
    path('entregables/', entregables, name="entregables"),
    path('curso-formulario/', form_con_api, name="FormularioCurso"),
    path('alumnos-formulario/', form_alumnos, name="FormularioEstudiantes"),
    path('profesores-formulario/', form_profesores, name="FormularioProfesores"),
    path('entregables-formulario/', form_entregables, name="FormularioEntregables"),
    path('busqueda-curso/',busquedaCurso, name="busquedaCurso"),
    path('buscar/',buscar),
    path('leerProfesores/',leerProfesores,name="LeerProfesores"),
    path('create_curso/', CursoCreateView.as_view(), name="CrearCurso"),
    path('actualizar/<pk>/', CursoUpdateView.as_view(), name = "ActualizarCurso"),
    path('borrar_curso/<pk>/', CursoDeleteView.as_view(), name = "BorrarCurso")
]