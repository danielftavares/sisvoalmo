# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader
from django.core import serializers
from django.forms import ModelForm
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from datetime import datetime, timedelta, date 

from models import *



@login_required
def index(request):
	t = loader.get_template('index.html')
	usuarios = Usuario.objects.all()
	restaurantes = Restaurante.objects.all()
	c = Context({
		'usuarios': usuarios,
		'restaurantes' : restaurantes,
		'usuariologado' : request.user
	})
	return HttpResponse(t.render(c))

@login_required
def votacao(request):
	dia = date.today()
	data = serializers.serialize('json',Voto.objects.filter(dia__gte =  dia.isoformat()), use_natural_keys=True)
	return HttpResponse(data)
	
@login_required
def votar(request):
	restaurante_pk = request.POST.get('restaurantepk')
	r = Restaurante.objects.get(pk=restaurante_pk)
	u = Usuario.objects.get(pk=request.user.pk)
	dia = date.today()
	
	v = Voto.objects.filter(usuario = u, dia = dia)
	
	if(len(v) == 0):
		v = Voto()
		v.usuario = u
		v.restaurante = r
		v.save()
	else:
		v = v[0]
		v.restaurante = r
		v.save()

	return HttpResponse("ok")
	
def mensagens(request):
	ultima_mensagem = request.POST.get('ultimamensagem')
	dia = date.today()
	data = serializers.serialize('json',Mensagem.objects.filter(pk__gt = ultima_mensagem,  dia = dia), use_natural_keys=True)
	return HttpResponse(data)
	
def enviarmensagens(request):
	u = Usuario.objects.get(pk=request.user.pk)
	m = Mensagem()
	m.usuario = u
	m.mensagem = request.POST.get('mensagem')
	m.save()