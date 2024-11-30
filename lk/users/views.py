from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm


def sign_in(request):
    print('start')
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user:
                print('auth')
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('profile')

        # form is not valid or user is not authenticated
        print(form.cleaned_data)
        messages.error(request, f'Invalid username or password')
        return render(request, 'registration/login.html', {'form': form})


def sign_up(request):
    form = RegisterForm()
    if request.method == 'GET':
        return render(request, 'registration/register.html', {'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form': form})
