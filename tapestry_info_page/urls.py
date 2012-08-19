from django.conf.urls import patterns, include, url
from tapestry_info_page.views import *
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
					   url(r'^$', 'tapestry_info_page.views.landing_page', name='landing_page'),
    # Examples:
    # url(r'^$', 'tapestry_info_page.views.home', name='home'),
    # url(r'^tapestry_info_page/', include('tapestry_info_page.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

#Serve static files
urlpatterns += patterns('',
                        (r'^tapestry_info_page/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                        )
