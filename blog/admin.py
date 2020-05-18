from django.contrib import admin
from django.utils.text import Truncator
from .models import Categorie, Article, Inscription

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug':('titre', ),}
    
    # Colonnes personalisees
    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caracteres du contenu de l'article, suivi
        de points de suspension, si le texte est plus long
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    #En tete de notre colonne
    apercu_contenu.short_description = 'Apercu du contenu'

    #configuration du formulaire d'administration
    fieldsets = (
        #Fieldst 1: meta-info (titre, auteur,categorie)
    ('General', {
        #classes :collapse pour permettre l'option d'afficher ou cacher
        'classes': ['collapse',],
        'fields':('titre', 'slug', 'auteur','categorie')
        }),
    #Fieldset 2: contenu de l'article
    ('Contenu de l\'article', {
        #description qui s'affiche au dessus du premier champ du fieldset
        'description': 'Le formulaire accepte les balises HTML, utilisez-les a bon escient!',
        'fields':('contenu',)
        }),
    )
    
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Inscription)
