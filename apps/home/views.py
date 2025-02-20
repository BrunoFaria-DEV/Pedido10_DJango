# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from .models import Cliente, FormaPGTO, Pedido, Produto


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))

#####################################################################
# Clientes                                                          #
#####################################################################
@login_required(login_url="/login/")
def clientes(request): 

    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, "home/clientes/clientes.html", context)

@login_required(login_url="/login/")
def clientes_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        Cliente.objects.create(Nome=nome, Email=email, Endereco=endereco)
        return redirect('clientes')

    return render(request, 'home/clientes/clientes_create.html')

@login_required(login_url="/login/")
def clientes_delete(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'home/clientes/clientes.html', {'cliente': cliente})

@login_required(login_url="/login/")
def clientes_edit(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)

    if request.method == 'POST':
        cliente.Nome = request.POST.get('nome')
        cliente.Email = request.POST.get('email')
        cliente.Endereco = request.POST.get('endereco')
        cliente.save()
        return redirect('clientes')

    context = {'cliente': cliente}
    return render(request, 'home/clientes/clientes_edit.html', context)


#####################################################################
# Produtos                                                          #
#####################################################################
@login_required(login_url="/login/")
def produtos(request): 

    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, "home/produtos/produtos.html", context)

@login_required(login_url="/login/")
def produtos_create(request):
    if request.method == 'POST':
        nome_produto = request.POST.get('nome_produto')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco')
        imagem = request.FILES.get('imagem')

        Produto.objects.create(Nome_Produto=nome_produto, Descricao=descricao, Preco=preco, Imagem=imagem)
        return redirect('produtos')

    return render(request, 'home/produtos/produtos_create.html')

@login_required(login_url="/login/")
def produtos_delete(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos')
    return render(request, 'home/produtos/produtos.html', {'produto': produto})

@login_required(login_url="/login/")
def produtos_edit(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'POST':
        produto.Nome_Produto = request.POST.get('nome_produto')
        produto.Descricao = request.POST.get('descricao')
        produto.Preco = request.POST.get('preco')
        if request.FILES.get('imagem'):
            produto.Imagem = request.FILES.get('imagem')
        produto.save()
        return redirect('produtos')

    context = {'produto': produto}
    return render(request, 'home/produtos/produtos_edit.html', context)

#####################################################################
# forma_pgtos                                                       #
#####################################################################
@login_required(login_url="/login/")
def forma_pgtos(request): 

    forma_pgtos = FormaPGTO.objects.all()
    context = {'forma_pgtos': forma_pgtos}
    return render(request, "home/forma_pgtos/forma_pgtos.html", context)

@login_required(login_url="/login/")
def forma_pgtos_create(request):
    if request.method == 'POST':
        desc_forma_pgto = request.POST.get('desc_forma_pgto')

        FormaPGTO.objects.create(Desc_Forma_PGTO=desc_forma_pgto)
        return redirect('forma_pgtos')

    return render(request, 'home/forma_pgtos/forma_pgtos_create.html')

@login_required(login_url="/login/")
def forma_pgtos_delete(request, forma_pgto_id):
    forma_pgto = get_object_or_404(FormaPGTO, pk=forma_pgto_id)
    if request.method == 'POST':
        forma_pgto.delete()
        return redirect('forma_pgtos')
    return render(request, 'home/forma_pgtos/forma_pgtos.html', {'forma_pgto': forma_pgto})

@login_required(login_url="/login/")
def forma_pgtos_edit(request, forma_pgto_id):
    forma_pgto = get_object_or_404(FormaPGTO, pk=forma_pgto_id)

    if request.method == 'POST':
        forma_pgto.Desc_Forma_PGTO = request.POST.get('desc_forma_pgto')

        forma_pgto.save()
        return redirect('forma_pgtos')

    context = {'forma_pgto': forma_pgto}
    return render(request, 'home/forma_pgtos/forma_pgtos_edit.html', context)

#####################################################################
# pedidos                                                           #
#####################################################################
@login_required(login_url="/login/")
def pedidos(request):
    pedidos = Pedido.objects.select_related('ID_Cliente', 'ID_Produto', 'ID_FormaPGTO').all()
    context = {'pedidos': pedidos}
    return render(request, "home/pedidos/pedidos.html", context)

@login_required(login_url="/login/")
def pedidos_create(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    formas_pagamento = FormaPGTO.objects.all()

    if request.method == 'POST':
        vlr_total_pedido = request.POST.get('vlr_total_pedido')
        pago = request.POST.get('pago')
        status_pedido = request.POST.get('status_pedido')
        dt_pedido = request.POST.get('dt_pedido')

        id_cliente = request.POST.get('id_cliente')
        id_produto = request.POST.get('id_produto')
        id_formapgto = request.POST.get('id_formapgto')

        cliente = get_object_or_404(Cliente, pk=id_cliente)
        produto = get_object_or_404(Produto, pk=id_produto)
        formapgto = get_object_or_404(FormaPGTO, pk=id_formapgto)

        Pedido.objects.create(
            VLR_Total_Pedido=vlr_total_pedido, 
            Pago=pago, 
            Status_Pedido=status_pedido,
            DT_Pedido=dt_pedido,
            ID_Cliente=cliente,
            ID_Produto=produto,
            ID_FormaPGTO=formapgto
        )
        return redirect('pedidos')

    context = {
        'clientes': clientes,
        'produtos': produtos,
        'formas_pagamento': formas_pagamento,
    }
    return render(request, 'home/pedidos/pedidos_create.html', context)

@login_required(login_url="/login/")
def pedidos_delete(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')
    return render(request, 'home/pedidos/pedidos.html', {'pedido': pedido})

@login_required(login_url="/login/")
def pedidos_edit(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    formas_pagamento = FormaPGTO.objects.all()

    if request.method == 'POST':
        vlr_total_pedido = request.POST.get('vlr_total_pedido')
        pago = request.POST.get('pago')
        status_pedido = request.POST.get('status_pedido')
        dt_pedido = request.POST.get('dt_pedido')

        id_cliente = request.POST.get('id_cliente')
        id_produto = request.POST.get('id_produto')
        id_formapgto = request.POST.get('id_formapgto')

        cliente = get_object_or_404(Cliente, pk=id_cliente)
        produto = get_object_or_404(Produto, pk=id_produto)
        formapgto = get_object_or_404(FormaPGTO, pk=id_formapgto)

        pedido.VLR_Total_Pedido = vlr_total_pedido
        pedido.Pago = pago
        pedido.Status_Pedido = status_pedido
        pedido.DT_Pedido = dt_pedido
        pedido.ID_Cliente = cliente
        pedido.ID_Produto = produto
        pedido.ID_FormaPGTO = formapgto
        pedido.save()

        return redirect('pedidos')

    context = {
        'pedido': pedido,
        'clientes': clientes,
        'produtos': produtos,
        'formas_pagamento': formas_pagamento,
    }
    return render(request, 'home/pedidos/pedidos_edit.html', context)