from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


#precisar ter uma url depois uma view e depois um template