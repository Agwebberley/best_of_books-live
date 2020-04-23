from django.db import models

# Create your models here.

def get_absolute_url(self):
	return reverse('home') 