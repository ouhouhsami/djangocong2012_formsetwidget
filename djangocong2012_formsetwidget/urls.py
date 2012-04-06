from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangocong2012_formsetwidget.views.home', name='home'),
    # url(r'^djangocong2012_formsetwidget/', include('djangocong2012_formsetwidget.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^places/', include('places.urls'))
)

urlpatterns += staticfiles_urlpatterns()

