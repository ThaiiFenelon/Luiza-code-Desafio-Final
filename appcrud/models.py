from django.db import models

class Empresas(models.Model):
    Nome_da_Empresa = models.CharField(max_length=255)
    Pais_de_Origem = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=20)
    def __str__(self):
        return self.Nome_da_Empresa + " - " + self.Pais_de_Origem + " - " + self.CNPJ

class Produtos(models.Model):
    Nome_do_Produto = models.CharField(max_length=255)
    Descricao = models.CharField(max_length=255)
    Preco = models.CharField(max_length=20)
    Empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)