from typing import Any, Dict
from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import ListView, DetailView, TemplateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: #usuario esta autenticado:
            # redireciona para a homefilmes
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) # redireciona para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')
        
class Homefilmes(LoginRequiredMixin, ListView):
    model = Filme
    template_name = 'homefilmes.html'
    context_object_name = 'filmes'
    paginate_by = 3

class DetalhesFilme(LoginRequiredMixin, DetailView):
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
    
class Pesquisafilme(LoginRequiredMixin, ListView):
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

class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')
    
class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
    
    
    
    
    
    
    
    
# def homepage(request):
#     return render(request, "homepage.html")

# url - view - html
# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all()
#     context['lista_filmes'] = lista_filmes
#     return render(request, "homefilmes.html", context)
        
        

