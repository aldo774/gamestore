from django import forms
from .models import Cadastro, CadastroPF, CadastroPJ, Contato

#TIPO_C = (('PF',u'Pessoa Fisica'),('PJ',u'Pessoa Juridica'),)

class Busca(forms.Form):
	Buscar = forms.CharField(max_length=100)

class FCadastroPF(forms.ModelForm):
	class Meta:
		model = CadastroPF
		fields = ['nome','sobrenome','email','endereco','num',\
		'bairro','cidade','cep','pais','senha','cpf','rg']

class FCadastroPJ(forms.ModelForm):
	class Meta:
		model = CadastroPJ
		fields = ['nome','razaoSocial','email','endereco','num',\
		'bairro','cidade','cep','pais','senha','cnpj']

class FCadastro(forms.ModelForm):
	class Meta:
		model = CadastroPF
		fields = ['nome','sobrenome','email','endereco','num',\
		'bairro','cidade','cep','pais','senha','cpf','rg']

class FContato(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ['nome','email','mensagem']