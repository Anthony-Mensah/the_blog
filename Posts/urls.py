from django.urls import path
from . import views
from .views import (PostListView,PostDetailView,PostCategoryListView,PostCreateView,CommentCreateView,PostDeleteView,PostUpdateView,UserListView)

urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	#post detail view
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	#post list category
	path('post/<str:name>/', PostCategoryListView.as_view(), name='post-category'),
	path('search/', views.search, name='search'),
	#post search
	path('create-post/', PostCreateView.as_view(), name='create-post'),
	#post comment
	path('post/<int:pk>/comment', CommentCreateView.as_view(), name='comment'),
	#post delete
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-post'),
	#post update
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update-post'),
	# USERS POST
	path('user/<str:username>/', UserListView.as_view(), name='user-post')

]