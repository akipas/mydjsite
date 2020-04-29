from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
       titre = models.CharField(max_length=100)
       auteur = models.CharField(max_length=50)
       contenu = models.TextField(null=True)
       date = models.DateTimeField(default=timezone.now,
                                   verbose_name='Date de publication')
       class Meta:
           ordering = ['date']
       def __str__(self) : 
            return self.titre
