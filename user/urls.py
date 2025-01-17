from django.contrib import admin
from django.urls import path
from .views import *
from user import views


urlpatterns = [
    path('', home, name='index'),
    path('home/', home, name='home'),
 ]
