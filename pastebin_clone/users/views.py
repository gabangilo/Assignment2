from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# user forms
def register(request):
    # validate form data when either a POST or GET form is requested
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)  # POST data

        if form.is_valid():  # if form is valid

            form.save()
            username = form.cleaned_data.get('username')  # clean data
            messages.success(request, f'Your account has been created you may login!')

            return redirect('blog-home')
    else:

        form = UserRegisterForm()  # empty form

    return render(request, 'users/register.html', {'form': form})

# users profile form
@login_required  # decorator that makes sure login is required to access profile
def profile(request):

    return render(request, 'users/profile.html')