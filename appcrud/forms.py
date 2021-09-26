from django.forms import ModelForm
from appcrud.models import Empresas, Produtos

class EmpresasForm(ModelForm):
     class Meta:
         model = Empresas
         fields = ['Nome_da_Empresa', 'Pais_de_Origem', 'CNPJ']

class ProdutosForm(ModelForm):
     class Meta:
         model = Produtos
         fields = ['Nome_do_Produto', 'Descricao', 'Preco']
