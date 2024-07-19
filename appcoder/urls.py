from django.urls import path
from appcoder.views import inicio, cursos, estudiantes, profesores, entregables

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('entregables/', entregables),
]