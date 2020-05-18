from django.urls import path
from . import views

urlpatterns = [
    path('',views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact',views.contact, name='contact'),
    path('ajouter',views.ajoutArticle, name='ajoutArticle'),
    path('inscription',views.nouveau_inscrit, name='nouveau_inscrit'),

]
