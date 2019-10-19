from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def blog(request):
    article = Article.objects.all()
    tags = Tag.objects.filter(statut=True)[:6]
    paginator = Paginator(article, 5)
    page = request.GET.get('page')
    articles =  paginator.get_page(page)
    nombre =  articles.paginator.num_pages
    data= {
        'article': article,
        'articles': articles,
        'tags': tags,
        'nombre':nombre,
    }
    return render(request, 'pages/blog.html', data)

def singleblog(request, id):
    
    articles = Article.objects.filter(pk=id)
    commentaire = Comentaire.objects.all()[:2]
    categorie = Categorie.objects.filter(statut=True)[:3]
    newsarticle = Article.objects.filter(statut=True).order_by('-id')
    
        
    data = {
        'article':articles,
        'newsarticle': newsarticle,
        'commentaire': commentaire, 
    }
    return render(request, 'pages/singleblog.html', data)

