from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name="store/index.html"
