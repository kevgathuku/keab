from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    """Render the Home Page Template"""

    template_name = 'index.html'
