# Generated by Django 5.0.7 on 2024-09-11 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('quantidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoFinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('horario', models.TimeField()),
                ('validade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdutoFinal', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto_Final', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.produtofinal')),
            ],
        ),
    ]
