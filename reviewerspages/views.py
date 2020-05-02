from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Reviewer
from django.urls import reverse_lazy
from mainapp.models import Post
# Create your views here.


class ReviewerBioView(ListView):
	model = Reviewer
	template_name = 'reviewer.html'
	ordering = ['-pub_date']
