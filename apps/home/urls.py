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

    path('produtos', views.produtos, name='produtos'),
    path('produtos/novo', views.produtos_create, name='produtos.create'),
    path('produtos/editar/<int:produto_id>/', views.produtos_edit, name='produtos.edit'),
    path('produtos/deletar/<int:produto_id>/', views.produtos_delete, name='produtos.delete'),

    path('forma_pgtos', views.forma_pgtos, name='forma_pgtos'),
    path('forma_pgtos/novo', views.forma_pgtos_create, name='forma_pgtos.create'),
    path('forma_pgtos/editar/<int:forma_pgto_id>/', views.forma_pgtos_edit, name='forma_pgtos.edit'),
    path('forma_pgtos/deletar/<int:forma_pgto_id>/', views.forma_pgtos_delete, name='forma_pgtos.delete'),

    path('pedidos', views.pedidos, name='pedidos'),
    path('pedidos/novo', views.pedidos_create, name='pedidos.create'),
    path('pedidos/editar/<int:pedido_id>/', views.pedidos_edit, name='pedidos.edit'),
    path('pedidos/deletar/<int:pedido_id>/', views.pedidos_delete, name='pedidos.delete'),
]