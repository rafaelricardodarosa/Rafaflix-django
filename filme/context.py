from .models import Filme

def lista_filmes_recentes(request):
    filmes_recentes = Filme.objects.all().order_by('-data_criacao')[0:3]
    return {'lista_filmes_recentes': filmes_recentes}

def lista_filmes_emalta(request):
    filmes_emalta = Filme.objects.all().order_by('-visualizacoes')[0:3]
    return {'lista_filmes_emalta': filmes_emalta}