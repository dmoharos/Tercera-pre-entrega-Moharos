from django.urls import path
from AppPreEntrega import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('materias/', views.materias, name= "Materias"),
    path('docentes/', views.docentes, name= "Docentes"),
    path('alumnos/', views.alumnos, name= "Alumnos"),
    #path('cursoFormulario/', views.cursoFormulario, name= "cursoFormulario"),
    #path('profesorFormulario/', views.profesorFormulario, name= "profesorFormulario"),
    #path('busquedaCamada/', views.busquedaCamada, name= "busquedaCamada"),
    #path('buscar/', views.buscar),
]