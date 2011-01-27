from django.conf.urls.defaults import *
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sisvoalmo/', include('sisvoalmo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^$', 'votacao.views.index'),
	(r'^ajax/votacao', 'votacao.views.votacao'),
	(r'^ajax/votar$', 'votacao.views.votar'),
	
	 (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	 (r'^admin/', include(admin.site.urls)),
	 (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
