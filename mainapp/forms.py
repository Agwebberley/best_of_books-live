from django import forms
from .models import Post, Genre

genres = Genre.objects.all().values_list('name', 'name')

genre_list = []


for genre in genres:
	genre_list.append(genre)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'reviewer', 'pub_date', 'genre', 'should_know', 'snippit',  'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			'reviewer': forms.Select(attrs={'class': 'form-control'}),
			'pub_date': forms.DateInput(attrs={'class': 'form-control'}), 
			'genre': forms.Select(choices=genre_list, attrs={'class': 'form-control'}),
			'should_know': forms.TextInput(attrs={'class': 'form-control'}),
			'snippit': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),



		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'author', 'pub_date', 'genre', 'should_know', 'snippit', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			#'reviewer': forms.Select(attrs={'class': 'form-control'}),
			'pub_date': forms.DateInput(attrs={'class': 'form-control'}), 
			'genre': forms.Select(choices=genre_list, attrs={'class': 'form-control'}),
			'should_know': forms.TextInput(attrs={'class': 'form-control'}),
			'snippit': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),




		}

