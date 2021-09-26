from django.shortcuts import render, redirect
from appcrud.forms import EmpresasForm, ProdutosForm
from appcrud.models import Empresas, Produtos
from django.core.paginator import Paginator

def home(request):
    data = {}
    search = request.GET.get('searchindex')
    if search:
        data['db'] = Empresas.objects.filter(Nome_da_Empresa__icontains=search)
    else:
        data['db'] = Empresas.objects.all()

    all = Empresas.objects.all()
    paginator = Paginator(all, 12)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)

    return render(request, 'index.html', data)

def form(request):
    data = {}
    data ['form'] = EmpresasForm()
    return render (request, 'form.html', data)

def create(request):
    form = EmpresasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)

    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    data['form'] = EmpresasForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    form = EmpresasForm(request.POST or None, instance=data['db'])
    if form .is_valid():
        form.save()
        return redirect('home')

def delete (request, pk):
    db = Empresas.objects.get(pk=pk)
    db.delete()
    return redirect ('home')

def homeprodutos(request, empresa_id):
    data = {}
    data['db'] = Produtos.objects.filter(Empresa=empresa_id)

    return render(request, 'indexprodutos.html', data)

def formprodutos(request, empresa_id):
    data = {}
    data ['formprodutos'] = ProdutosForm()
    data ['empresa_id'] = empresa_id
    return render (request, 'formprodutos.html', data)

def createprodutos(request):
    formprodutos = ProdutosForm(request.POST or None)
    if formprodutos.is_valid():
        formprodutos.save()
        return redirect('indexprodutos.html')

def viewprodutos(request, pk):
    data = {}
    data['db'] = Produtos.objects.filter(pk=pk)
    
    return render(request, 'viewprodutos.html', data)

def produtos_empresa(request, empresa_id):
    data = {}
    data['db'] = Produtos.objects.filter(Empresa=empresa_id)
    data['empresa_id'] = empresa_id
    
    return render(request, 'produtos_empresa.html', data)

def editprodutos(request, empresa_id):
    data = {}
    data['db'] = Produtos.objects.get(Empresa=empresa_id)
    data['formprodutos'] = ProdutosForm(instance=data['db'])
    return render(request, 'formprodutos.html', data)

def updateprodutos(request, empresa_id):
    data = {}
    data['db'] = Produtos.objects.get(Empresa=empresa_id)
    formprodutos = ProdutosForm(request.POST or None, instance=data['db'])
    if formprodutos .is_valid():
        formprodutos.save()
        return redirect('indexprodutos.html')

def deleteprodutos (request, empresa_id):
    db = Produtos.objects.get(Empresa=empresa_id)
    db.delete()
    return redirect ('indexprodutos.html')