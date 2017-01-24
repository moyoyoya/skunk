from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, ProfileForm, RelationForm, UserForm, InformationForm
from .models import Profile, Information
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, instance=Profile)
        information_form = InformationForm(request.POST, instance=Information)
        if user_form.is_valid() and profile_form.is_valid() and information_form.is_valid():
            # Create a new user without saving it
            new_user = user_form.save(commit=False)
            #add password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile_form.save(commit=False)
            profile_form.user = new_user
            profile_form.save()
            information_form.save(commit=False)
            information_form.user = new_user
            information_form.save()
            return render(request, 'account/register_done.html', {'new_user': new_user, 'profile_form': profile_form,
                                                                  'information_form': information_form})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm(instance=Profile())
        information_form = InformationForm(instance=Information())
    return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form,
                                                     'information_form': information_form})

@login_required
def edit(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        user_form = UserForm(instance=request.user, data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

