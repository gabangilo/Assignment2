from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    title = models.CharField(max_length = 100)  # char field max
    content = models.TextField()  # text field for unrestricted lines of text
    date_posted = models.DateTimeField(default = timezone.now)  # uses default dating for posts
    author = models.ForeignKey(User, on_delete = models.CASCADE)  # if user is deleted posts are as well

    #  post object more desc
    def __str__(self):
        return self.title