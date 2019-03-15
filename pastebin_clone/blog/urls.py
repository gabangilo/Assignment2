from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

# maps to urls of project
urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),  # path to homepage
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),  # path to unique post based on pk int
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),  # path to post creation
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),  # path to post update based on pk int
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),  # path to post delete based on pk int
    path('about/', views.about, name = 'blog-about'),  # path to about page
]