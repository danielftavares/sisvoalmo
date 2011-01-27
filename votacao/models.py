from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(User):
	def natural_key(self):
		return (self.pk, self.username)

class Restaurante(models.Model):
	nome = models.CharField(max_length=20)
	notaComida = models.IntegerField()
	notaAtendimento = models.IntegerField()
	def natural_key(self):
		return (self.pk, self.nome, self.notaComida, self.notaAtendimento)


class Voto(models.Model):
	usuario = models.ForeignKey(Usuario)
	restaurante = models.ForeignKey(Restaurante)
	dia = models.DateField(auto_now_add=True)
	def natural_key(self):
		return (self.pk, self.usuario, self.restaurante, self.dia)
		
class Mensagem(models.Model):
	mensagem = models.CharField(max_length=100)
	usuario = models.ForeignKey(Usuario)
	dia = models.DateField(auto_now_add=True)
	def natural_key(self):
		return (self.pk, self.mensagem, self.usuario, self.dia)