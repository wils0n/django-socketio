from django.shortcuts import render

from django.views.generic import *


class TestView(TemplateView):
    template_name = 'message/index.html'

class SendMessageView(TemplateView):
    template_name = 'message/send-message.html'