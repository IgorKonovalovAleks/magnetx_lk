from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('profile', profile_view, name='profile'),
]
