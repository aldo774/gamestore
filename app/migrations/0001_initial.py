# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=4)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=8)),
                ('pais', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mensagem', models.TextField(max_length=2000)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='item')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
                ('qtd', models.IntegerField(default=0)),
                ('visu', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='Data de Publicacao')),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nome_plataforma', models.CharField(max_length=30)),
                ('imagem', models.ImageField(upload_to='plataforma')),
                ('pagina', models.CharField(max_length=30, default='/item/')),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('ddd', models.IntegerField()),
                ('telefone', models.CharField(max_length=20)),
                ('ramal', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vis',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('itm', models.ForeignKey(to='app.Item')),
            ],
        ),
        migrations.CreateModel(
            name='CadastroPF',
            fields=[
                ('cadastro_ptr', models.OneToOneField(serialize=False, parent_link=True, to='app.Cadastro', primary_key=True, auto_created=True)),
                ('rg', models.CharField(blank=True, max_length=9, null=True)),
                ('cpf', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name_plural': 'Cadastros Pessoas Fisicas',
                'verbose_name': 'Cadastro Pessoa Fisica',
            },
            bases=('app.cadastro',),
        ),
        migrations.CreateModel(
            name='CadastroPJ',
            fields=[
                ('cadastro_ptr', models.OneToOneField(serialize=False, parent_link=True, to='app.Cadastro', primary_key=True, auto_created=True)),
                ('razaoSocial', models.CharField(max_length=100, verbose_name='Razao Social')),
                ('cnpj', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ['razaoSocial'],
                'verbose_name_plural': 'Cadastros Pessoas Juridicas',
                'verbose_name': 'Cadastro Pessoa Juridica',
            },
            bases=('app.cadastro',),
        ),
        migrations.AddField(
            model_name='vis',
            name='usu',
            field=models.ForeignKey(null=True, to='app.Cadastro'),
        ),
        migrations.AddField(
            model_name='telefone',
            name='cadastro',
            field=models.ForeignKey(to='app.Cadastro'),
        ),
        migrations.AddField(
            model_name='item',
            name='nome_plataforma',
            field=models.ForeignKey(to='app.Plataforma'),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='user',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, editable=False, blank=True),
        ),
    ]
