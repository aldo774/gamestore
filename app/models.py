from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

#TIPO_C = (('PF',u'Pessoa Fisica'),('PJ',u'Pessoa Juridica'),)

class Plataforma(models.Model):
	nome_plataforma = models.CharField(max_length = 30)
	imagem = models.ImageField(upload_to = "plataforma")
	pagina = models.CharField(max_length = 30, default="/item/")

	def __str__(self):
		return self.nome_plataforma


class Item(models.Model):
	imagem = models.ImageField(upload_to = "item")
	nome_plataforma = models.ForeignKey(Plataforma)
	nome = models.CharField(max_length = 100)
	preco = models.DecimalField(max_digits=6,decimal_places=2)
	qtd = models.IntegerField(default=0)
	visu = models.IntegerField(default=0)
	pub_date = models.DateTimeField('Data de Publicacao')

	def __str__(self):
		return self.nome

class Contato(models.Model):
	nome = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	mensagem = models.TextField(max_length=2000)

	class Meta:
		ordering = ['nome']

	def __str__(self):
		return self.email

class Cadastro(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, editable=False)

	nome = models.CharField(max_length=20)
	sobrenome = models.CharField(max_length=80)
	email = models.EmailField(max_length=100)
	endereco = models.CharField(max_length=100)
	num = models.CharField(max_length=4)
	bairro = models.CharField(max_length=50)
	cidade = models.CharField(max_length=30)
	cep = models.CharField(max_length=8)
	pais = models.CharField(max_length=20)
	senha = models.CharField(max_length=15)
#	tipopessoa = models.CharField(max_length=2, verbose_name='Tipo',choices=TIPO_C, blank=True, null="True")
	#datacadastro = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-id']

	def save(self):
		if not self.id:
			c = Cadastro.objects.filter(email=self.email).count()
			if c:
				raise EmailExistente

			usr = User.objects.filter(username=self.email)
			if usr:
				u = usr[0]
			else:
				u = User.objects.create_user(self.email, self.email, self.senha, first_name=self.nome)
			u.save()
			self.user = u
		else:
			self.user.username = self.email
			self.user.email = self.email
			self.user.set_password(self.senha)
			self.user.first_name = self.nome
			self.user.save()

		super(Cadastro, self).save()

	def __str__(self):
		return self.nome

class CadastroPF(Cadastro):
	rg = models.CharField(max_length=9, null=True,blank=True)
	cpf = models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = u'Cadastro Pessoa Fisica'
		verbose_name_plural = u'Cadastros Pessoas Fisicas'
		ordering = ['nome']

class CadastroPJ(Cadastro):
	razaoSocial = models.CharField(max_length=100,verbose_name=u'Razao Social')
	cnpj = models.CharField(max_length=11)

	def __str__(self):
		return self.razaoSocial

	class Meta:
		verbose_name = u'Cadastro Pessoa Juridica'
		verbose_name_plural = u'Cadastros Pessoas Juridicas'
		ordering = ['razaoSocial']

class Vis(models.Model):
	usu = models.ForeignKey(Cadastro, null=True)
	itm = models.ForeignKey(Item)

	def __str__(self):
		return self.itm.nome

class Telefone(models.Model):
	cadastro = models.ForeignKey(Cadastro)
	ddd = models.IntegerField()
	telefone = models.CharField(max_length=20)
	ramal = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return '(%s) %s - %s' %(self.ddd,self.telefone,self.ramal,)

