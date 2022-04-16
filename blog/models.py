from django.db import models

# Create your models here.

class Curso (models.Model):
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()
    

    def __str__(self):
        return self.nombre
class Estudiante (models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.lastname}"

class Profesor (models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
         return f"{self.name} {self.lastname}"
    