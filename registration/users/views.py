from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import SignUpForm, LoginForm
from .models import CustomUser
from django.contrib import messages  # Add this import

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Mark the user as active
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})





def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['username']
            password = form.cleaned_data['password']

            
            user = None
            if '@' in identifier:
                user = CustomUser.objects.filter(email=identifier).first()
            elif identifier.isdigit():
                user = CustomUser.objects.filter(phone_number=identifier).first()
            else:
                user = CustomUser.objects.filter(username=identifier).first()

            if user is not None:
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def home(request):
    return render(request, 'users/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')