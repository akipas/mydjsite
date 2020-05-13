from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Article
from .forms import ContactForm

# Create your views here.
def accueil(request):
    """Afficher tous les articles"""
    articles = Article.objects.all()
    return render(request, 'blog/accueil.html', {'derniers_articles':articles})

def lire(request, id, slug):
    """afficher l'article en entier"""
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})
 
def contact(request):
    """costruction du formulaire avec les donnees de l'utilisateur ou vide si l'utilisateur accede pour la premiere fois"""
    form = ContactForm(request.POST or None)
    #verification des donnees envoyees
    #le methode envoie False s'il n'ya pas de donnees dans le formulaire
    #ou qu'il contien des erreurs
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = forrm.claened_data['renvoi']

        #envoi de l'e-mail grace aux donnees que nous venons de recuperer
        envoi = True

    #affichage de la page du formulaire
    return render(request,'blog/contact.html', locals())
