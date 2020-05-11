from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Article

# Create your views here.
def accueil(request):
    """Afficher tous les articles"""
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles':articles})

def lire(request, id):
    """afficher l'article en entier"""
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})
 
