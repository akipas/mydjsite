from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from blog.models import Article,Inscription
from .forms import ContactForm, ArticleForm, InscriptionForm

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
    #la methode envoie False s'il n'ya pas de donnees dans le formulaire
    #ou qu'il contien des erreurs
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = forrm.claened_data['renvoi']

        #envoi de l'e-mail grace aux donnees que nous venons de recuperer
        envoi = True

    #affichage de la page du formulaire
    return render(request,'blog/contact.html', locals())

def ajoutArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        titre = form.cleaned_data['titre']
        slug = form.cleaned_data['slug']
        auteur = form.cleaned_data['auteur']
        contenu = form.cleaned_data['contenu']
        categorie = form.cleaned_data['categorie']
        form.save()
        return HttpResponse('succes')
        
    return render(request, 'blog/ajouterA.html',locals())

def nouveau_inscrit(request):
    #sauvegarde = False
    #ajout d'un argument request.FILES qui recueille les donnees autre que le texte, Ici photo
    form = InscriptionForm(request.POST or None, request.FILES)
    if form.is_valid():
        #inscrit = Inscription()
        nom = form.cleaned_data['nom']
        adresse = form.cleaned_data['adresse']
        photo = form.cleaned_data['photo']
        form.save()
        #sauvegarde = True
        return HttpResponse('succes')
    return render(request, 'blog/inscription.html', locals())

def liste_inscription(request):
    return render(
        request,
        'blog/liste.html',
        {'inscriptions': Inscription.objects.all()}
    )

    
