from django.shortcuts import render
from .models import Filme
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.


class Homepage(TemplateView):
    template_name = 'homepage.html'

class Homefilmes(ListView):
    model = Filme
    template_name = 'homefilmes.html'
    context_object_name = 'filmes'
    paginate_by = 3

class DetalhesFilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme

