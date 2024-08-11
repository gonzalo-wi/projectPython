from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import *
from appcoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.
def inicio(request):
    return render(request,"appcoder/inicio.html")

def cursos(request):
    return render(request, "appcoder/cursos.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision = informacion["camada"])
            curso.save()
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = CursoFormulario()
    return render(request, "appcoder/form_cursos.html",{"mi_formulario": mi_formulario})


def form_alumnos(request):
    if request.method == "POST":
        mi_formulario = EstudiantesFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido = informacion["apellido"])
            estudiante.save()
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = EstudiantesFormulario()
    return render(request, "appcoder/form_alumnos.html",{"mi_formulario": mi_formulario})

def form_profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesoresFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion["nombre"], apellido = informacion["apellido"])
            profesor.save()
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = ProfesoresFormulario()
    return render(request, "appcoder/form_profesores.html",{"mi_formulario": mi_formulario})

def form_entregables(request):
    if request.method == "POST":
        mi_formulario = EntregablesFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            entregable = Entregable(nombre=informacion["nombre"])
            entregable.save()
            return render(request, "appcoder/inicio.html")
    else:
        mi_formulario = EntregablesFormulario()
    return render(request, "appcoder/form_entregables.html",{"mi_formulario": mi_formulario})

def busquedaCurso(request):
    return render(request, "appcoder/busquedaCurso.html")

def buscar(request):
    if request.GET['comision']:
        comision = request.GET['comision']
        cursos = Curso.objects.filter(comision__icontains=comision)
        return render(request, "appcoder/busquedaCurso.html", {"cursos":cursos,"comision":comision})
    else:
        respuesta="No enviaste datos"
    return HttpResponse(respuesta)

def leerProfesores(request):
    profesores = Profesor.objects.all()
    return render(request,"appcoder/leerProfesores.html",{"profesores": profesores})

class CursoListView(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/cursos.html"

class CursoCreateView(CreateView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/create_curso.html"
    success_url = reverse_lazy("cursos")
    fields = ["nombre","comision"]

class CursoUpdateView(UpdateView):
    model = Curso
    context_object_name = "cursos"
    template_name = "appcoder/actualizar.html"
    fields = ["nombre","comision"]  
    success_url = reverse_lazy("cursos")

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "appcoder/borrar_curso.html"
    success_url = reverse_lazy("cursos")
     
      
