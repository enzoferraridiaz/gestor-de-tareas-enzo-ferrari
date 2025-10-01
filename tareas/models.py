
from django.db import models


class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    prioridad = models.IntegerField(default=3)
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateField(null=True, blank=True)


    class Meta: 
        ordering = ['-fecha_creacion']


    def __str__(self):
        return f"{self.titulo} (prioridad {self.prioridad})"
    ## creamos modelo