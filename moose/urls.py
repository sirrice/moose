from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'moose.views.home', name='home'),
    url(r'^question/$', 'moose.views.question', name='question'),
    url(r'^question/(\w+)/$', 'moose.views.question', name='question'),
    url(r'^dashboard/$', 'moose.views.dashboard', name='dashboard'),    
    # url(r'^moose/', include('moose.foo.urlsax')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
