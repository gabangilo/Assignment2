from django.shortcuts import render
from .models import Post

#  posting structure for html
posts = [
    {
        'author': 'Gabe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Mar 10 2019',
    },
    {
        'author': 'Sam',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Mar 11 2019',
    }
]

# home url content
def home(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)

# about url content
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


