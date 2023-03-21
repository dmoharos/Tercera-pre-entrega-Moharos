from django.urls import path
from AppPreEntrega import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('materias/', views.materias, name= "Materias"),
    path('docentes/', views.docentes, name= "Docentes"),
    path('alumnos/', views.alumnos, name= "Alumnos"),
    path('buscar/', views.buscar),
    
    #path('materiaFormulario/', views.materiaFormulario, name= "materiaFormulario"),
    #path('docenteFormulario/', views.docenteFormulario, name= "docenteFormulario"),
    #path('alumnoFormulario/', views.alumnoFormulario, name= "alumnoFormulario"),
    #path('busquedaComision/', views.busquedaComision, name= "busquedaComision"),
    
]