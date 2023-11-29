from django.urls import path
from .views import *

urlpatterns= [

#Clientes
    path ('cliente/listar', listar_clientes, name = 'listar_clientes'),
    path ('cliente/listar/<int:id>', listar_clientes_id, name = 'listar_clientes_id'),
    path ('cliente/inserir', inserir_clientes, name = 'inserir_clientes'),
    path ('cliente/remover_clientes/<int:id>', remover_clientes, name = 'remover_clientes'),
    path('cliente/editar/<int:id>', editar_clientes, name='editar_clientes'),
#Produtos
    path ('produto/listar', listar_produtos, name = 'listar_produtos'),
    path ('produto/listar/<int:id>', listar_produtos_id, name = 'listar_produtos_id'),
    path ('produto/inserir', inserir_produtos, name = 'inserir_produtos'),
    path ('produto/remover_produtos/<int:id>', remover_produtos, name = 'remover_produtos'),

#Vendedores
    path ('vendedor/listar', listar_vendedores, name = 'listar_vendedores'),
    path ('vendedor/listar/<int:id>', listar_vendedores_id, name = 'listar_vendedores_id'),
    path ('vendedor/inserir', inserir_vendedores, name = 'inserir_vendedores'),
    path ('vendedor/remover_vendedores/<int:id>', remover_vendedores, name = 'remover_vendedores'),

#Pedidos
    path ('pedido/listar', listar_pedidos, name = 'listar_pedidos'),
    path ('pedido/listar/<int:id>', listar_pedidos_id, name = 'listar_pedidos_id'),
    path ('pedido/inserir', inserir_pedidos, name = 'inserir_pedidos'),
    path ('pedido/remover_pedidos/<int:id>', remover_pedidos, name = 'remover_pedidos')

]