from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
from django.contrib.auth import authenticate, logout, login as Authlogin
from django.template import Context, loader, RequestContext
from .models import Plataforma, Item, Cadastro, Vis
from django.http import Http404, HttpResponseRedirect
from .forms import Busca, FCadastroPF, FCadastroPJ, FContato
from django.core.urlresolvers import reverse

def index(request):
		plt = Plataforma.objects.order_by('nome_plataforma')
		dest = Item.objects.order_by('-visu')[:5]
		nov = Item.objects.order_by('-pub_date')[:5]
		form = Busca()
		pltdic = {'plt': plt, 'nov': nov, 'dest': dest, 'form': form}
		return render(request, 'item/index.html', pltdic)

def PS3Itens(request):
		plt = Plataforma.objects.order_by('nome_plataforma')
		itm = Item.objects.filter(nome_plataforma__nome_plataforma='PS3')
		form = Busca()
		itmdic = {'itm': itm, 'plt': plt, 'form': form}
		return render(request, 'item/PS3Itens.html', itmdic)

def Xbox360Itens(request):
		plt = Plataforma.objects.order_by('nome_plataforma')
		itm = Item.objects.filter(nome_plataforma__nome_plataforma='Xbox 360')
		form = Busca()
		itmdic = {'itm': itm, 'plt': plt, 'form': form}
		return render(request, 'item/Xbox360Itens.html', itmdic)

def buscar(request):
	f = Busca()
	b = False
	form = Busca(request.GET or None)
	if form.is_valid():
		b = form.cleaned_data.get("Buscar")
	plt = Plataforma.objects.order_by('nome_plataforma')
	itm = Item.objects.filter(nome__contains=b)
	dest = Item.objects.order_by('-visu')[:3]
	itmdic = {'plt': plt,'itm': itm, 'f':f, 'dest': dest}
	return render(request, 'item/buscar.html', itmdic)

def cadastro(request):
	form = FCadastroPF()
	f = Busca()
	dest = Item.objects.order_by('-visu')[:3]
	plt = Plataforma.objects.order_by('nome_plataforma')
	pltdic = {'form': form, 'f': f, 'dest': dest, 'plt': plt}
	return render(request, 'item/cadastro.html', pltdic)

def itmvisu(request, item_id):
	t = ''
	plt = Plataforma.objects.order_by('nome_plataforma')
	form = Busca()
	itm = Item.objects.order_by('-visu')[:3]
	e = 'Guardado'
	try:
		item = Item.objects.get(pk=item_id)
		if request.user.is_active:
			if not request.user.is_staff:
				c = Cadastro.objects.get(user__first_name=request.user.first_name)
				t = Vis.objects.filter(itm=item,usu=c)


	except item.DoesNotExist:
		raise Http404("Item nao existe")

	else:
		if len(t) == 0:
			e = 'Guardar'
		item.visu += 1
		item.save()

	return render(request, 'item/itemVisu.html',{'item': item,'e':e, 'plt': plt, 'form': form,'itm': itm})

def hist(request, item_id):
	try:
		#item = Item.objects.get(pk=item_id)
		item = get_object_or_404(Item, pk=item_id)
		if request.user.is_active:
			if not request.user.is_staff:
				c = Cadastro.objects.get(user__first_name=request.user.first_name)

	except (KeyError, item.DoesNotExist):
		return render(request, 'item/itemVisu.html', {
			'error_message': "Pagina nao encontrada.",
			})

	else:
		if request.user.is_active:
			if not request.user.is_staff:
				t = Vis.objects.filter(itm=item,usu=c)
				if len(t) == 0:
					v = Vis.objects.create(itm=item,usu=c)
					v.save()

	return HttpResponseRedirect(reverse('item:hist', args=(item.id,)))


def cadastro2(request):
	form = FCadastroPJ()
	f = Busca()
	dest = Item.objects.order_by('-visu')[:3]
	plt = Plataforma.objects.order_by('nome_plataforma')
	pltdic = {'form': form, 'f': f, 'dest': dest, 'plt': plt}
	return render(request, 'item/cadastro2.html', pltdic)


def ncadastro(request):
	form = FCadastroPF(request.POST or None)
	form.save()
	return render_to_response("item/ncadastro.html",locals(),context_instance=RequestContext(request))

def ncadastro2(request):
	form = FCadastroPJ(request.POST or None)
	form.save()
	return render_to_response("item/ncadastro2.html",locals(),context_instance=RequestContext(request))


def login(request):

	if request.user.id:
		return render_to_response('item/logado.html',(),context_instance=RequestContext(request, {}))

	if request.POST:
		emailUser = request.POST.get('email')
		senhaUser = request.POST.get('senha')
		u = authenticate(username=emailUser, password=senhaUser)
		if u is not None:
			if u.is_active:
				Authlogin(request, u)

				if request.POST.get('next'):
					return HttpResponseRedirect(request.POST.get('next'))

				return render_to_response('item/logado.html',(),context_instance=RequestContext(request, {}))

	return render_to_response('item/login.html',(),context_instance=RequestContext(request, {}))

def sair(request):
	logout(request)
	return render_to_response('item/logout.html',(),context_instance=RequestContext(request, {}))

def ban(request):
	return render(request, 'item/ban.html')

def rod(request):
	return render(request, 'item/rod.html')

def menu(request):
	return render(request, 'item/menu.html')

def contato(request):
	form = FContato()
	f = Busca()
	dest = Item.objects.order_by('-visu')[:3]
	plt = Plataforma.objects.order_by('nome_plataforma')
	pltdic = {'form': form, 'f': f, 'dest': dest, 'plt': plt}
	return render(request, 'item/contato.html', pltdic)

def contato2(request):
	form = FContato(request.POST or None)
	form.save()
	return render_to_response("item/contato2.html",locals(),context_instance=RequestContext(request))

def guardados(request):
	t = ''
	plt = Plataforma.objects.order_by('nome_plataforma')
	form = Busca()
	itm = Item.objects.order_by('-visu')[:3]

	try:
		if request.user.is_active:
			if not request.user.is_staff:
				c = Cadastro.objects.get(user__first_name=request.user.first_name)
				t = Vis.objects.filter(usu=c)


	except item.DoesNotExist:
		raise Http404("Item nao existe")

	else:
		if not t:
			return render(request, 'item/guardados.html',{'plt': plt, 'form': form,'itm': itm})		
	
	return render(request, 'item/guardados.html',{'plt': plt, 't': t, 'form': form,'itm': itm})
