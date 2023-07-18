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
        return context #retorna o contexto de filmes relacionados
    
    #contador de visualizacoes dos episodios
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super(DetalhesFilme, self).get(request, *args, **kwargs) #retorna o contexto de visualizacoes
    
class Pesquisafilme(ListView):
    template_name = "pesquisa.html"
    model = Filme

    # Sobrescrevendo o método get_queryset para filtrar os filmes pelo termo de pesquisa,deixando preciso a pesquisa
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None
        
        

