from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'post_date',  'author', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.Select(attrs={'class': 'form-control'}),
			'post_date': forms.DateInput(attrs={'class': 'form-control'}), 
			'body': forms.Textarea(attrs={'class': 'form-control'}),



		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'post_date',  'body',)

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'post_date': forms.DateInput(attrs={'class': 'form-control'}), 
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),




		}

