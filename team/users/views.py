from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import NewRegisterForm
from .models import User_Profile
# Import your UserProfile form
from .forms import ProfileForm
# Create your views here.
def register(request): 

    if request.method == "POST":
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('users:profile')  
    else:
        form = NewRegisterForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context) 


def success(request):
    return render(request,"users/success.html")

from django.shortcuts import render, redirect
from .forms import ProfileForm



def user_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            # Associate the UserProfile with the current user
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('users:success')
    else:
        form = ProfileForm()
    return render(request, 'users/profile.html', {'form': form})
