"""projetofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appcrud.views import deleteprodutos, home, form, formprodutos, produtos_empresa, create, createprodutos, view, edit, editprodutos, update, updateprodutos, delete, deleteprodutos, viewprodutos, homeprodutos

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

    path('empresa/<int:empresa_id>/produtos/', produtos_empresa, name='produtos_empresa'),
    path('empresa/<int:empresa_id>/produtos/formprodutos/', formprodutos, name='formprodutos'),
    path('empresa/<int:empresa_id>/produtos/createprodutos/', createprodutos, name='createprodutos'),
    path('viewprodutos/<int:empresa_id>/produtos', viewprodutos, name='viewprodutos'),
    path('editprodutos/<int:empresa_id>/produtos', editprodutos, name='editprodutos'),
    path('updateprodutos/<int:empresa_id>/produtos', updateprodutos, name='updateprodutos'),
    path('deleteprodutos/<int:empresa_id>/produtos', deleteprodutos, name='deleteprodutos'),
]
