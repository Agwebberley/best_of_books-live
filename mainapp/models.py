from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
	title = models.CharField(max_length=255)
	rating = models.CharField(max_length=1)
	author = models.CharField(max_length=255)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
	post_date = models.DateField()
	should_know = models.CharField(max_length=255)
	body = models.TextField()
	def __str__(self):
		return self.title + ' | ' + str(self.author)
	def get_absolute_url(self):
		return reverse('article-detail', args=(str(self.id)))