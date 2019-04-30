from django.db import models


class Mascota(models.Model):
    folio = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
