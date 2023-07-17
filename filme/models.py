from django.db import models


# Create your models here.
# criar o filme
Lista_Categorias = (
    ("ANALISES", "Analises"),
    ("PROGRAMACAO", "Programacao"),
    ("APRESENTACAO", "Apresentacao"),
    ("OUTROS", "Outros"),    
)
       
class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    thumb = models.ImageField(upload_to='thumb_filmes', null=True, blank=True) #selecionar a pasta aonde vai salvar a imagem
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=Lista_Categorias)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
    
# criar os episodios

class Episodio(models.Model):
    titulo = models.CharField(max_length=255)
    video = models.URLField(max_length=255)
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name="episodios") 
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo
    
    #on_delete=models.CASCADE - deletar o episodio quando o filme for deletado
    # related_name="episodios" - para poder acessar os episodios do filme
    
    
# criar o usuario