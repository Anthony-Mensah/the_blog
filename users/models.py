from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	twitter_url = models.CharField(max_length=200, null=True, blank=True)
	facebook_url = models.CharField(max_length=200, null=True, blank=True)
	instagram_url = models.CharField(max_length=200, null=True, blank=True)
