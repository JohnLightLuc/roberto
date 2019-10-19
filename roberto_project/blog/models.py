from django.db import models

from tinymce import HTMLField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=100 )
    image = models.ImageField(upload_to='Categorie')
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=50)
    statut = models.BooleanField(default=False)
    
class Tag(models.Model):
    nom = models.CharField(max_length=100 )
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=False)
    
class Article(models.Model):
    titre = models.CharField(max_length=100 )
    autheur = models.CharField(max_length=50 )
    categorie = models.name = models.ForeignKey('Categorie', related_name='article_categorie', on_delete=models.CASCADE)
    tag = models.name = models.ForeignKey('Tag', related_name='article_tag', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Article')
    content= HTMLField('Content')
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=False)
        
    
class Comentaire(models.Model):
    user = models.CharField( max_length=50)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='comment', default ='image.jpg')
    article = models.name = models.ForeignKey(Article, related_name='comment_article', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_up = models.DateTimeField(auto_now=True)
    statut = models.BooleanField(default=False)

    