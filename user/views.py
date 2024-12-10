from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from skill.models import Course, UserProfile
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been created, you can now login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
        return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password.")
            return render(request, 'user/login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'user/login.html', {'form': form})

@login_required
def update_profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"Your profile has been updated successfully!")
            return redirect('login')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'user/update_profile.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')

def dashboard_view(request):
    user=UserProfile.objects.all()
    courses=Course.objects.all()
    return render(request, 'admin_dashboard.html', {'user': user, 'courses': courses})

