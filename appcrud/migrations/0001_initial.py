# Generated by Django 3.2.7 on 2021-09-24 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_da_Empresa', models.CharField(max_length=255)),
                ('Pais_de_Origem', models.CharField(max_length=100)),
                ('CNPJ', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome_do_Produto', models.CharField(max_length=255)),
                ('Descricao', models.CharField(max_length=255)),
                ('Preco', models.CharField(max_length=20)),
                ('Empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcrud.empresas')),
            ],
        ),
    ]
