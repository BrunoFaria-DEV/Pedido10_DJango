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
from .models import Cliente


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

@login_required(login_url="/login/")
def clientes(request): 

    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, "home/clientes.html", context)

@login_required(login_url="/login/")
def clientes_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')

        Cliente.objects.create(Nome=nome, Email=email, Endereco=endereco)
        return redirect('clientes')

    return render(request, 'home/clientes_create.html')

@login_required(login_url="/login/")
def clientes_delete(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'home/confirm_delete.html', {'cliente': cliente})

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
    return render(request, 'home/clientes_edit.html', context)
