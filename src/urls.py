# -*- coding: utf8 -*-

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', include('website.urls')),


    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
