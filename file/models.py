from django.db import models

# Create your models here.

class FileModel(models.Model):
    tipo = models.CharField(max_length=26)
    data = models.CharField(max_length=26)
    valor = models.CharField(max_length=26)
    CPF = models.CharField(max_length=14)
    cartao = models.CharField(max_length=26)
    hora = models.CharField(max_length=9)
    dono = models.CharField(max_length=30)
    nome_loja = models.CharField(max_length=26)