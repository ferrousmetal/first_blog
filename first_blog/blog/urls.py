from django.urls import path
from blog.views import *
app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('post/<pk>/', detail, name='detail'),
    path('archives/<int:year>/<int:month>/', archives, name='archives'),
    path('category/<pk>/', category, name='category'),
    path('tag<pk>/', tag, name='tag'),
    path('search/', search, name='search'),
    path('about', about, name='about'),

]
