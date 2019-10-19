# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'date_add',
        'date_up',
        'user',
        'statut',
    )
    list_filter = (
        'date_add',
        'date_up',
        'statut',
        'id',
        'nom',
        'image',
        'date_add',
        'date_up',
        'user',
        'statut',
    )


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_up', 'statut')
    list_filter = (
        'date_add',
        'date_up',
        'statut',
        'id',
        'nom',
        'date_add',
        'date_up',
        'statut',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'titre',
        'autheur',
        'categorie',
        'tag',
        'image',
        'content',
        'date_add',
        'date_up',
        'statut',
    )
    list_filter = (
        'categorie',
        'tag',
        'date_add',
        'date_up',
        'statut',
        'id',
        'titre',
        'autheur',
        'categorie',
        'tag',
        'image',
        'content',
        'date_add',
        'date_up',
        'statut',
    )


class ComentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'content',
        'article',
        'date_add',
        'date_up',
        'statut',
    )
    list_filter = (
        'article',
        'date_add',
        'date_up',
        'statut',
        'id',
        'user',
        'content',
        'article',
        'date_add',
        'date_up',
        'statut',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Tag, TagAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Comentaire, ComentaireAdmin)
