from django.db import models
from django.utils import timezone
from django.db.models import Model

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom
    
class Article(models.Model):
       titre = models.CharField(max_length=100)
       slug = models.SlugField(max_length=100, null=True)
       auteur = models.CharField(max_length=50)
       contenu = models.TextField(null=True)
       date = models.DateTimeField(default=timezone.now,
                                   verbose_name='Date de publication')
       categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
       class Meta:
           ordering = ['date']
       def __str__(self) : 
            return self.titre

class Inscription(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    #dossier "photo/" va se creer automatiquement des le 1er enregistrement
    photo = models.ImageField(upload_to="photo/")

    def __str__(self):
        return self.nom

class Moteur(models.Model):
    nom = models.CharField(max_length=25)
    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur =models.OneToOneField(Moteur, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
    
