from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Genre, reviewers
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
	model = Post
	template_name = "home.html"
	ordering = ['-pub_date']

	#if 'search' in request.GET:
	#	search_term = request.GET['search']
	#	posts = post.filter(text__icontains="search_term")

	#ordering = ['-id']

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'


class AddGenreView(CreateView):
	model = Genre
	template_name = 'add_genre.html'
	fields = '__all__'


class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'

class DeletePostView(DeleteView):
	model = Post
	success_url = reverse_lazy('home')
	template_name = 'delete_post.html'


#class reviewerview(ListView):
#	model = reviewers
#	template_name = "reviewer_details.html"
#	ordering = ['-pub_date']

class reviewerhomeview(ListView):
	model = reviewers
	template_name = "reviewer_home.html"

def GenreView(request, genres):
	genre_posts = Post.objects.filter(genre=genres)
	#ordering = ['-pub_date']
	return render(request, 'genres.html', {"genres":genres.title(), 'genre_posts':genre_posts})


def ReviewerView(request, reviewer):
	reviewer_posts = Post.objects.filter(reviewer=reviewer)
	reviewer = Reviewer.objects.filter(reviewer__username = reviewer)

	#ordering = ['-pub_date']
	#u = User.objects.get(username=username)
	return render(request, 'reviewer-details.html', {"reviewers":reviewers, 'reviewer_posts':reviewer_posts})