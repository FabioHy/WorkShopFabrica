from django.db import models

# Create your models here.


class Musico(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Instrumento(models.Model):
    modelo = models.CharField(max_length=50)
    quantidade = models.IntegerField(default='1')

    def __str__(self):
        return self.modelo




