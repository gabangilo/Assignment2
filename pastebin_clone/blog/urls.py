from django.urls import path
from . import views

# maps to urls of project
urlpatterns = [
    path('', views.home, name='blog-home'),  # path to homepage
    path('about/', views.about, name='blog-about'),
]