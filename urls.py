from django.conf.urls.defaults import patterns, include, url
from moose.models import SHORTNAME_PATTERN

import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'moose.views.home', name='home'),
    url(r'^moose/a/', include('registration.backends.email.urls')),
    url(r'^moose/', include('moose.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.ASSETS_ROOT}),
    url('(%s)/$' % (SHORTNAME_PATTERN), 'moose.views.feedback', name='feedback'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/$', include(admin.site.urls)),
)
