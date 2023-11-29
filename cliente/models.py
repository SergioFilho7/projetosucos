from django.db import models
from django_cpf_cnpj.fields import CNPJField, CPFField
from datetime import datetime
from django.utils import formats

class Cliente(models.Model):
    cpf=CPFField(masked=True)
    cnpj=CNPJField(masked=True)
    nome_cliente=models.CharField(max_length=100)
    endereco_cliente=models.CharField(max_length=50)
    bairro_cliente=models.CharField(max_length=30)
    cidade_cliente=models.CharField(max_length=30)
    cep_cliente=models.CharField(max_length=9)
    data_nascimento=models.DateField()
    limite_credito=models.DecimalField(max_digits=7, decimal_places=2)
    primeira_compra=models.BooleanField()
    def __str__(self):
        return f'{self.cpf}'
    
class Produto(models.Model):
    cod_produto=models.CharField(max_length=14)
    nome_produto=models.CharField(max_length=100)
    embalagem=models.CharField(max_length=20)
    tamanho=models.CharField(max_length=20)
    sabor=models.CharField(max_length=10)
    preco_lista=models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return f'{self.cod_produto}'
    
class Vendedor(models.Model):
    cod_vendedor=models.CharField(max_length=14)
    nome_vendedor=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.cod_vendedor}'
    

class Pedido(models.Model):
    cod_pedido=models.CharField(max_length=14)
    cod_vendedor=models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cpf=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cod_produto=models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco_lista=models.DecimalField(Produto, max_digits=7, decimal_places=2)
    quantidade=models.IntegerField()
    def __str__(self):
        return f'{self.cod_pedido}'
