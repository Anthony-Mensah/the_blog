from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (ListView,DetailView,CreateView,DeleteView,UpdateView)
from .models import Post, Category, Comment
from .forms import PostCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User

# Create your views here.

# LIST VIEW
class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	ordering = '-datePosted'
	paginate_by = 6

# DETAIL VIEW
class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'

# CATEGORY VIEW
class PostCategoryListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'Posts/post_category.html'
	paginate_by = 6

	def get_queryset(self):
		category_name = get_object_or_404(Category, name=self.kwargs.get('name'))
		return Post.objects.filter(category=category_name).order_by('-datePosted')

# USER LIST VIEW
class UserListView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'Posts/user_post.html'
	paginate_by = 6

	def get_queryset(self):
		username = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=username).order_by('-datePosted')


# SEARCH LIST VIEW
def search(request):
	if request.method == "POST":
		search_name = request.POST['search']
		posts = Post.objects.filter(title__contains=search_name)
		return render(request, "Posts/search.html",{"posts":posts, "search_name":search_name})
	else:
		return render(request, "Posts/search.html")

# POST CREATE VIEW
class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	form_class = PostCreateForm

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

# COMMENT CREATE VIEW
class CommentCreateView(CreateView):
	model = Comment
	fields = ['commentor_name','context']
	template_name = 'Posts/comment.html'
	success_url = '/'

	def form_valid(self,form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

# DELETE POST
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	context_object_name = 'post'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False

# UPDATE POST
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	form_class = PostCreateForm

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			return False
