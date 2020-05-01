from django.urls import path
#from . import views
from .views import HomeView, AddPostView, ArticleDetailView, GenreView, UpdatePostView, DeletePostView, AddGenreView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
from django.conf.urls import include



sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [


    path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
	path('', HomeView.as_view(), name="home"),
	path('article/<slug:slug>', ArticleDetailView.as_view(), name='article-detail'),
	path('add_post/', AddPostView.as_view(), name="add_post"),
	path('article/edit/<slug:slug>', UpdatePostView.as_view(), name="update_post"),
	path('article/delete/<slug:slug>', DeletePostView.as_view(), name="delete_post"),
	path(r'info', 
    TemplateView.as_view(template_name='info.html'),
    name='info'),
    path(r'about', 
    TemplateView.as_view(template_name='about.html'),
    name='about'),
    path('add_genre/', AddGenreView.as_view(), name="add_genre"),
    path('genre/<str:genres>', GenreView, name="genre"),





]

