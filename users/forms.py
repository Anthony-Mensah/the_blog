from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

# USER UPDATE FORM
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

# PROFILE UPDATE FORM
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image','twitter_url','facebook_url','instagram_url']
