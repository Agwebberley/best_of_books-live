from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'rating', 'post_date', 'reviewer', 'author', 'should_know', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			'reviewer': forms.Select(attrs={'class': 'form-control'}),
			'rating (1 to 5)': forms.TextInput(attrs={'class': 'form-control'}),
			'post_date': forms.DateInput(attrs={'class': 'form-control'}), 
			'should_know': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),



		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'rating', 'post_date', 'author', 'should_know', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control'}),
			#'reviewer': forms.Select(attrs={'class': 'form-control'}),
			'rating (1 to 5)': forms.TextInput(attrs={'class': 'form-control'}),
			'post_date': forms.DateInput(attrs={'class': 'form-control'}), 
			'should_know': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),




		}

