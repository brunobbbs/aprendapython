# -*- coding: utf8 -*-

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # Home Page
    url(r'^$', direct_to_template,
        {'template': 'website/index.html'}, name='homepage'),
)
