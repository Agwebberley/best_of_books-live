from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Genre(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, null=False, unique=True)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
	author = models.CharField(max_length=255)
	pub_date = models.DateField()
	genre = models.CharField(max_length=255)
	should_know = models.CharField(max_length=500)
	snippit = models.CharField(max_length=255)
	body = models.TextField()
	def __str__(self):
		return self.title + ' | ' + str(self.author)
	def get_absolute_url(self):
		return reverse('home')

class reviewers(models.Model):
	reviewer = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField()



	def __str__(self):
		return self.reviewer.username 
	def get_absolute_url(self):
		return reverse('home')