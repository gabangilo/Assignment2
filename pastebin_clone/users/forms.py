from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# custom register form design
class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    # used to save fields to the model in order
    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']

# custome update form for user (name, email)
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField()

    # used to save fields to the model in order
    class Meta:

        model = User
        fields = ['username', 'email']

# custome update form for profile
class ProfileUpdateForm(forms.ModelForm):

    # used to save fields to the model in order
    class Meta:

            model = Profile
            fields = ['image']