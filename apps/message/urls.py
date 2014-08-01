__author__ = 'wils0n'

from django.conf.urls import patterns, include, url
from .views import *
from django.views.generic import *

urlpatterns = patterns('',
                       url(r'^$', TestView.as_view()),
                       url(r'^send/message/$', SendMessageView.as_view()),
                       )
