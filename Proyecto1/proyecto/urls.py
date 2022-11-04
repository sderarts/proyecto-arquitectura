from django.contrib import admin
from django.urls import path
from .views import login_user,register_user,home,logout_request

urlpatterns = [
    path('login_user',login_user,name="login"),
    path('register_user',register_user,name="register"),
    path('home',home,name="home"),
    path('logout',logout_request,name="logout"),

]
