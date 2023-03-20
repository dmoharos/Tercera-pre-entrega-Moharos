from django import forms

class MateriaFormulario(forms.Form):
    materia= forms.CharField()
    comision= forms.IntegerField()
    
class DocenteFormulario(forms.Form):
    nombre= forms.CharField(max_length= 30)
    apellido= forms.CharField(max_length= 30)
    correo= forms.EmailField()
    
class AlumnoFormulario(forms.Form):
    nombre= forms.CharField(max_length= 30)
    apellido= forms.CharField(max_length= 30)
    correo= forms.EmailField()