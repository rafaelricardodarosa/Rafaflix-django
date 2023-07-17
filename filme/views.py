from typing import Any, Dict
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
    
    # Sobrescrevendo o método get_context_data para passar o contexto de filmes relacionados
    def get_context_data(self, **kwargs: Any):
        context = super(DetalhesFilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.object.categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context

