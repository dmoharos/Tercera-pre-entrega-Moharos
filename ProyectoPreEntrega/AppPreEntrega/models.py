from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre= models.CharField(max_length= 40)
    comision= models.IntegerField()

class Docente(models.Model):
    nombre= models.CharField(max_length= 30)
    apellido= models.CharField(max_length= 30)
    correo= models.EmailField()
    
class Alumno(models.Model):
    nombre= models.CharField(max_length= 30)
    apellido= models.CharField(max_length= 30)
    correo= models.EmailField()
