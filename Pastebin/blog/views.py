from django.shortcuts import render
from .models import Post 
#posts = [
#	{
#		'author': 'Michal',
#		'title':	'blog 1',
#		'content':	'First post',
#		'date_posted':	'March 10, 2019'
#	},
def home(request):
	context = {
		'posts': Post.objects.all()	
	}
	return render(request, 'blog/home.html', context)
	

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

