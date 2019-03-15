from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# create fields for users
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):  # User object more desc

        return f'{self.user.username} Profile'

    #  saves image with new dimensions from parent class
    def save(self):

        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:

            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)