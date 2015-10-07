from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^PS3Itens/$', views.PS3Itens, name='PS3Itens'),
	url(r'^Xbox360Itens/$', views.Xbox360Itens, name='Xbox360Itens'),
	url(r'^(?P<item_id>[0-9]+)/$', views.itmvisu, name='itmvisu'),
	url(r'^buscar/$', views.buscar, name='buscar'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.sair, name='sair'),
	url(r'^cadastro/$', views.cadastro, name='cadastro'),
	url(r'^cadastro2/$', views.cadastro2, name='cadastro2'),
	url(r'^ncadastro/$', views.ncadastro, name='ncadastro'),
	url(r'^ncadastro2/$', views.ncadastro2, name='ncadastro2'),
	url(r'^(?P<item_id>[0-9]+)/hist/$', views.hist, name='hist'),
	url(r'^ban/$', views.ban, name='ban'),
	url(r'^rod/$', views.rod, name='rod'),
	url(r'^menu/$', views.menu, name='menu'),
	url(r'^contato/$', views.contato, name='contato'),
	url(r'^contato2/$', views.contato2, name='contato2'),
	url(r'^guardados/$', views.guardados, name='guardados'),
]
