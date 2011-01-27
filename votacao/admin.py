from votacao.models import *
from django.contrib import admin

admin.site.register(Usuario)
admin.site.register(Voto)
admin.site.register(Mensagem)


class RestauranteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'notaComida')

admin.site.register(Restaurante, RestauranteAdmin)