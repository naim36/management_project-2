from django.contrib import admin
from django.urls import path
from .views import *
from user import views


urlpatterns = [
    path('', home),
    path('home', home),
]
