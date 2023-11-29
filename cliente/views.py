from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.http import HttpResponse
from .forms import ClienteForm
from .forms import Cliente
from django.shortcuts import render, get_object_or_404
from django.utils.datetime_safe import datetime
from django.utils.dateparse import parse_date
from decimal import Decimal
from datetime import datetime


#função tabela Cliente
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'listar_clientes.html',{'clientes': clientes} )

def listar_clientes_id(request, id):
    clientes_id = Cliente.objects.get(id=id)
    return render(request, 'listar_clientes_id.html',{'clientes_id': clientes_id} )

def inserir_clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'inserir_clientes.html', {'form': form})

def remover_clientes(request, id):
    clientes=Cliente.objects.get(id=id)
    if request.method=='POST':
        clientes.delete()
        return redirect('listar_clientes')
    return render(request, 'remover_clientes.html', {'clientes': clientes})


def editar_clientes(request, id):
    clientes=Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request,'inserir_clientes.html', {'form':form})

#Função tabela Produto
def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def listar_produtos_id(request, id):
    produtos_id = Produto.objects.get (id=id)
    return render (request, 'listar_produtos_id.html',{'produtos_id' : produtos_id})

def inserir_produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'inserir_produtos.html', {'form': form})

def remover_produtos(request, id):
    produtos=Produto.objects.get(id=id)
    if request.method=='POST':
        produtos.delete()
        return redirect('listar_produtos')
    return render(request, 'remover_produtos.html', {'produtos': produtos})

def editar_produtos(request, id):
    clientes=Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    return render(request,'inserir_produtos.html', {'form':form})

#Função tabela Pedido
def listar_pedidos(request):
    pedidos = Pedido.objects.all ()
    return render (request, 'listar_pedidos.html', {'pedidos': pedidos})

def listar_pedidos_id(request, id):
    pedidos_id = Pedido.objects.get (id=id)
    return render(request, 'listar_pedidos_id.html',{'pedidos_id' : pedidos_id})

def inserir_pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'inserir_pedidos.html', {'form': form})

def remover_pedidos(request, id):
    pedidos=Pedido.objects.get(id=id)
    if request.method=='POST':
        pedidos.delete()
        return redirect('listar_pedidos')
    return render(request, 'remover_pedidos.html', {'pedidos': pedidos})

def editar_pedidos(request, id):
    clientes=Pedido.objects.get(id=id)
    form = PedidoForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request,'inserir_pedidos.html', {'form':form})

#Função tabela Vendedor
def listar_vendedores(request):
    vendedores = Vendedor.objects.all ()
    return render(request, 'listar_vendedores.html', {'vendedores': vendedores})

def listar_vendedores_id(request, id):
    vendedores_id = Vendedor.objects.get (id=id)
    return render(request, 'listar_vendedores_id.html',{'vendedores_id': vendedores_id})

def inserir_vendedores(request):
    if request.method == 'POST':
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vendedores')
    else:
        form = VendedorForm()
    return render(request, 'inserir_vendedores.html', {'form': form})

def remover_vendedores(request, id):
    vendedores=Vendedor.objects.get(id=id)
    if request.method=='POST':
        vendedores.delete()
        return redirect('listar_vendedores')
    return render(request, 'remover_vendedores.html', {'vendedores': vendedores})

def editar_vendedores(request, id):
    clientes=Vendedor.objects.get(id=id)
    form = VendedorForm(request.POST or None, instance=clientes)
    if form.is_valid():
        form.save()
        return redirect('listar_vendedores')
    return render(request,'inserir_vendedores.html', {'form':form})