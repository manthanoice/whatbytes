from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    try:
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserRegistrationForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid username or password.')
        else:
            form = LoginForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
    return render(request, 'users/login.html', {'form': form})

@login_required(login_url='/please_login/')
def dashboard(request):
    try:
        return render(request, 'users/dashboard.html')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('login')

@login_required(login_url='/please_login/')
def profile(request):
    try:
        return render(request, 'users/profile.html')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('login')

def user_logout(request):
    try:
        logout(request)
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
    return redirect('login')

def please_login(request):
    try:
        return render(request, 'users/please_login.html')
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        return redirect('login')