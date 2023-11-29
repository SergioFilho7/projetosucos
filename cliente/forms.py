from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'cnpj', 'nome_cliente', 'endereco_cliente', 'bairro_cliente', 'cidade_cliente', 'cep_cliente', 'data_nascimento', 'limite_credito', 'primeira_compra']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['cod_produto', 'nome_produto', 'embalagem', 'tamanho', 'sabor', 'preco_lista']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['cod_vendedor', 'nome_vendedor']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cod_pedido', 'cod_vendedor', 'cpf', 'cod_produto', 'preco_lista', 'quantidade']