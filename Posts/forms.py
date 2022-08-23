from django import forms
from .models import Post, Category

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['image','category','title','content']

		widgets = {
			'title':forms.TextInput(attrs={'placeholder':'Enter post title'}),
			'category':forms.Select()
		}
