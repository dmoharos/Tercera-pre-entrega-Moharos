from django.urls import path
from AppPreEntrega import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('materias/', views.materias, name= "Materias"),
    path('docentes/', views.docentes, name= "Docentes"),
    path('alumnos/', views.alumnos, name= "Alumnos"),
    
    #path('materiaFormulario/', views.materiaFormulario, name= "materiaFormulario"),
    #path('docenteFormulario/', views.docenteFormulario, name= "docenteFormulario"),
    #path('alumnoFormulario/', views.alumnoFormulario, name= "alumnoFormulario"),
    
    #path('busquedaCamada/', views.busquedaCamada, name= "busquedaCamada"),
    #path('buscar/', views.buscar),
]