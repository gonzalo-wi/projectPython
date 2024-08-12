from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
   

    def __str__(self):
       return f"Nombre del curso: {self.nombre} - Numero de comision: {self.comision}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
       return f"Nombre del estudiante: {self.nombre} {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)
    def __str__(self):
       return f"Nombre del profesor: {self.nombre} {self.apellido}  - Email: {self.email} - Profesion: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return f"Nombre de entrega: {self.nombre} - Fecha de entrega: {self.fecha_de_entrega} - Entregado: {self.entregado}"   
