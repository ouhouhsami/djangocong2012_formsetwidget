from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^list/$', 'places.views.list', name='list'),
    url(r'^edit/(?P<placetype_slug>[-\w]+)$', 'places.views.edit', name='edit'),
    url(r'^read/(?P<placetype_slug>[-\w]+)$', 'places.views.read', name='read'),
)