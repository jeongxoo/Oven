from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

class MainpageView(TemplateView):
    template_name = "main.html"
