from django.db import models
class Docente (models.Model):
	codigo = models.TextField()
	nombre = models.TextField()
	dni = models.TextField()
	Fecha_nacimiento = models.TextField()
	Fecha_registro = models.DateTimeField(auto_now_add=True)
	estado =  models.TextField(max_length=1)



