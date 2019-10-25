# roberto_projet
## Comment acceder a un class fille a partir de la class mere 

Houff, enfin la solution:

Class 

  class Categorie(models.Model):
      nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
   
  class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, relatted_name='article_cat')
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return self.titre
   

   
   Solution
   
 
   1
   cat = Categorie.objects.get(pk=2)
   articles = cat.article_set.all() #passage par le nom de la classe
   
   2
   cat = Categorie.objects.get(pk=2)
   articles = cat.article_cat.all() #passage par related name
   
 
