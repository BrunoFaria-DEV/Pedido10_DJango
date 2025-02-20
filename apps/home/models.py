# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FormaPGTO(models.Model):
    Desc_Forma_PGTO = models.CharField(max_length=15)

    def __str__(self):
        return self.Desc_Forma_PGTO

class Produto(models.Model):
    Nome_Produto = models.CharField(max_length=50)
    Descricao = models.CharField(max_length=150)
    Preco = models.DecimalField(max_digits=9, decimal_places=2)
    Imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.Nome_Produto

class Cliente(models.Model):
    Nome = models.CharField(max_length=100)
    Email = models.EmailField(max_length=50)
    Endereco = models.CharField(max_length=150)

    def __str__(self):
        return self.Nome

class Pedido(models.Model):
    VLR_Total_Pedido = models.DecimalField(max_digits=9, decimal_places=2)
    Pago = models.CharField(max_length=10)
    Status_Pedido = models.CharField(max_length=10)
    DT_Pedido = models.DateField()
    ID_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ID_Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ID_FormaPGTO = models.ForeignKey(FormaPGTO, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)