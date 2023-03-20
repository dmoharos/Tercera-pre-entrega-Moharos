from django.shortcuts import render
from django.http import HttpResponse
from AppPreEntrega.models import Materia, Docente, Alumno
from AppPreEntrega.forms import MateriaFormulario, DocenteFormulario, AlumnoFormulario

# Create your views here.

def inicio(request):
    return render(request, "AppPreEntrega/inicio.html")

#def materias(request):
    #return render(request, "AppPreEntrega/materias.html")

#def docentes(request):
    #return render(request, "AppPreEntrega/docentes.html")

#def alumnos(request):
    #return render(request, "AppPreEntrega/alumnos.html")

def materias(request):    
    if request.method == "POST":
        miFormulario = MateriaFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            materia= Materia(nombre= informacion["materia"], comision= informacion["comision"])
            materia.save()
            return render(request, "AppPreEntrega/inicio.html")
    else:
        miFormulario= MateriaFormulario()
    
    return render(request, "AppPreEntrega/materias.html", {"miFormulario": miFormulario})

def docentes(request):
    if request.method == "POST":
        miFormulario = DocenteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            docente= Docente(nombre= informacion["nombre"], apellido= informacion["apellido"], correo= informacion["correo"])
            docente.save()
            return render(request, "AppPreEntrega/inicio.html")
    else:
        miFormulario= DocenteFormulario()
    
    return render(request, "AppPreEntrega/docentes.html", {"miFormulario": miFormulario})

def alumnos(request):
    if request.method == "POST":
        miFormulario = AlumnoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
    
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            alumno= Alumno(nombre= informacion["nombre"], apellido= informacion["apellido"], correo= informacion["correo"])
            alumno.save()
            return render(request, "AppPreEntrega/inicio.html")
    else:
        miFormulario= AlumnoFormulario()
    
    return render(request, "AppPreEntrega/alumnos.html", {"miFormulario": miFormulario})

"""
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