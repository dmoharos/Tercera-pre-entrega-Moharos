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
        miFormulario= MateriaFormulario(request.POST)
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
        miFormulario= DocenteFormulario(request.POST)
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
        miFormulario= AlumnoFormulario(request.POST)
    
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            alumno= Alumno(nombre= informacion["nombre"], apellido= informacion["apellido"], correo= informacion["correo"])
            alumno.save()
            return render(request, "AppPreEntrega/inicio.html")
    else:
        miFormulario= AlumnoFormulario()
    
    return render(request, "AppPreEntrega/alumnos.html", {"miFormulario": miFormulario})


#def busquedaComision(request):
    #return render(request, "AppPreEntrega/busquedaComision.html")


def buscar(request):
    if request.GET["comision"]:
        comision= request.GET['comision']
        materias= Materia.objects.filter(comision__icontains= comision)
        return render(request, "AppPreEntrega/resultadosBusqueda.html", {"materias": materias, "comision": comision})
    else:
        respuesta= "No enviaste datos"
        
    return render(request, "AppPreEntrega/inicio.html", {"respuesta": respuesta})
