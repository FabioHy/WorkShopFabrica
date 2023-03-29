from django.db import models

# Create your models here.

class LuisAmigo (models.Model):
    atividade = models.CharField(max_length=120)
    status = models.BooleanField(default=False)
