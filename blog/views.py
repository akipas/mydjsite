from django.shortcuts import render
from django.http import Http404
from blog.models import Article

# Create your views here.
def accueil(request):
    """Afficher tous les articles"""
     articles = Article.objects.all()
     return render(request, 'blog/accueil.html', {'derniers_articles':articles})

def lire(request, id):
    """afficher l'article en entier"""
    pass
 
