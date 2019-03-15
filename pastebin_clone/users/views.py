from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# user forms
def register(request):
    # validate form data when either a POST or GET form is requested
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)  # POST data

        if form.is_valid():  # if form is valid

            form.save()
            username = form.cleaned_data.get('username')  # clean data
            messages.success(request, f'Your account has been created you may login!')

            return redirect('login')
    else:

        form = UserRegisterForm()  # empty form

    return render(request, 'users/register.html', {'form': form})

# users profile form
@login_required  # decorator that makes sure login is required to access profile
def profile(request):

    # when form is submitted data will be sent
    if request.method == 'POST':

        user_form = UserUpdateForm(request.POST, instance= request.user)  # defines form for user update with data population
        profile_form = ProfileUpdateForm(request.POST,
                                         request.FILES,
                                         instance= request.user.profile)  # defines for profile update with data population

        if user_form.is_valid() and profile_form.is_valid():  # if form is valid saves form

            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:

        user_form = UserUpdateForm(instance=request.user)  # keep instance
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context)