from django.db import models
import datetime

# Create your models here.

class Noticias (models.Model):
    encabezado = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    autor = models.CharField(max_length=100, blank=False, null=False)
    fecha_creacion = models.DateField(default=datetime.date.today, blank=False, null=False)

    def _str_(self):
        return self.encabezado

class Descargas (models.Model):
    nombre_descarga = models.CharField(max_length=100, blank=False, null=False)
    enlace = models.URLField(blank=False, null=False, default="/https:wikipedia")

    def _str_(self):
        return self.nombre_descarga





class Actualizacion (models.Model):
    nombre_act = models.CharField(max_length=100, blank=False, null=False)
    fecha_act = models.DateField(default=datetime.date.today, blank=False, null=False)

    def _str_(self):
        return self.nombre_act


class Comentarios (models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    website = models.CharField(max_length=120, blank=False, null=False)
    comentario = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = ("Comement")
        verbose_name_plural = ("Comments")

    def _str_(self):
        return self.nombre
    
