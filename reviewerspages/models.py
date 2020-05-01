from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Reviewer(models.Model):
	reviewer = models.OneToOneField(User, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=255, null=False, unique=True)
	bio = models.TextField()



	def __str__(self):
		return self.slug
	def get_absolute_url(self):
		return reverse('home')