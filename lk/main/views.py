from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterForm


# Create your views here.


def index(request):
    return HttpResponse('<h4>2134</h4>')


def profile_view(request):
    return render(request, 'main/profile.html')
