from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('', views.blog , name='blog'),
    path('<int:id>/single-blog/', views.singleblog, name='singleblog'),

]