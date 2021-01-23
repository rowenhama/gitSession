from django.contrib import admin
from django.urls import path

from . import views

app_name = 'kasiraiLogin'
urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
]