from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# custom register form design
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    # used to save fields to the model in order
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']