# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

    path('clientes', views.clientes, name='clientes'),
    path('clientes/novo', views.clientes_create, name='clientes.create'),
    path('clientes/editar/<int:cliente_id>/', views.clientes_edit, name='clientes.edit'),
    path('clientes/deletar/<int:cliente_id>/', views.clientes_delete, name='clientes.delete'),

    # path('produtos', views.produtos, name='produtos'),
    # path('produtos/novo', views.produtos_create, name='produtos.create'),
    # path('produtos/editar', views.produtos_edit, name='produtos.edit'),
    # path('produtos/deletar', views.produtos_delete, name='produtos.delete'),

]
