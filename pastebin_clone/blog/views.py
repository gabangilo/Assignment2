from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin

# home url content
def home(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

# making posts into list format
class PostListView(ListView):

    model = Post
    template_name = 'blog/home.html'  # template used for post list
    context_object_name = 'posts'  # define object to post for list
    ordering = ['-date_posted']  # posts will be newest top ranging to oldest bottom
    paginate_by = 10 # display the 10 most recent posts

# view user posts
class UserPostListView(ListView):

    model = Post
    template_name = 'blog/user_posts.html'  
    context_object_name = 'posts'  # define object to post for list
    paginate_by = 10 # display the 10 most recent posts

    def get_queryset(self):
        # if user does not exists return a 404
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# chosen posts in detail
class PostDetailView(DetailView):

    model = Post

# user create post
class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    fields = ['title', 'content']

    # makes sure new blog post is done by current login by overriding form valid method
    def form_valid(self, form):

        form.instance.author = self.request.user  # makes the form part if the current instanced author

        return super().form_valid(form)  # validates the form by running the form_valid function against parent class

# user updates posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    fields = ['title', 'content']

    # makes sure new blog post is done by current login by overriding form valid method
    def form_valid(self, form):

        form.instance.author = self.request.user  # makes the form part if the current instanced author

        return super().form_valid(form)  # validates the form by running the form_valid function against parent class

    # test if correct user is trying to update
    def test_func(self):

        post = self.get_object()  # get current post

        if self.request.user == post.author:  # check if user is owner of post

            return True  # if true allow updating

        return False  # if false block updating

# user post deletion
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    success_url = '/'

    # test if correct user is trying to delete
    def test_func(self):
        post = self.get_object()  # get current post

        if self.request.user == post.author:  # check if user is owner of post

            return True  # if true allow deleting

        return False  # if false block deleting

# about url content
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


