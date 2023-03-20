from django.shortcuts import render
from django.http import HttpResponse
from AppPreEntrega.models import Materia, Docente, Alumno
#from AppPreEntrega.forms import CursoFormulario, ProfesorFormulario 

# Create your views here.

def inicio(request):
    return render(request, "AppPreEntrega/inicio.html")

def materias(request):
    return render(request, "AppPreEntrega/materias.html")

def docentes(request):
    return render(request, "AppPreEntrega/docentes.html")

def alumnos(request):
    return render(request, "AppPreEntrega/alumnos.html")

"""
def cursos(request):    
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            curso= Curso(nombre= informacion["curso"], camada= informacion["camada"])
            curso.save()
            return render(request, "AppPreEntrega/inicio.html")
    else:
        miFormulario= CursoFormulario()
    
    return render(request, "AppPreEntrega/cursos.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            profesor= Profesor(nombre= informacion["nombre"], apellido= informacion["apellido"], email= informacion["email"], profesion= informacion["profesion"])
            profesor.save()
            return render(request, "AppPreEntrega/inicio.html")
    else:
        miFormulario= ProfesorFormulario()
    
    return render(request, "AppPreEntrega/profesorFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppPreEntrega/busquedaCamada.html")

def buscar(request):
    #respuesta= f"Estoy buscando la camada nro: {request.GET['camada']}"
    if request.GET["camada"]:
        camada= request.GET['camada']
        cursos= Curso.objects.filter(camada__icontains= camada)
        return render(request, "AppPreEntrega/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        respuesta= "No enviaste datos"

    #return HttpResponse(respuesta)
    return render(request, "AppPreEntrega/inicio.html", {"respuesta": respuesta})
"""