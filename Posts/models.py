from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# CATEGORY MODEL
class Category(models.Model):
	name = models.CharField(max_length=200, default='OTHERS')

	def __str__(self):
		return self.name

# POST MODEL
class Post(models.Model):
	image = models.ImageField(default='default.jpg', upload_to='post_pics')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	datePosted = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=40)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

# COMMENT MODEL
class Comment(models.Model):
	commentor_name = models.CharField(max_length=25)
	dateCommented = models.DateTimeField(auto_now_add=True)
	context = models.TextField()
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

	def __str__(self):
		return self.commentor_name
