from django.urls import path
#from . import views
from .views import HomeView, AddPostView, ArticleDetailView, UpdatePostView, DeletePostView
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap


sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [


    path('sitemap.xml/', sitemap, {'sitemaps' : sitemaps } , name='sitemap'),
	path('', HomeView.as_view(), name="home"),
	path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
	path('add_post/', AddPostView.as_view(), name="add_post"),
	path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
	path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
	path(r'info', 
    TemplateView.as_view(template_name='info.html'),
    name='info'),
    path(r'about', 
    TemplateView.as_view(template_name='about.html'),
    name='about'),



]

