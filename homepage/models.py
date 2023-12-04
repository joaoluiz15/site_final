from django.db import models

# Create your models here.

class Cliente(models.Model):
    cpf = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)

class Carro(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    nome = models.CharField(max_length=20)
    ano_fabricacao = models.IntegerField()
    categoria = models.CharField(max_length=10)
    nome_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)





