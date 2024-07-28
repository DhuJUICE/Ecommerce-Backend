from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('login/loginButton', views.loginButton, name='loginButton2'),
    path('register/', views.register, name='register'),
    path('loginButton/', views.loginButton, name='loginButton'),
    path('registerButton', views.registerButton, name='registerButton'),
    path('register/registerButton', views.registerButton, name='registerButton2'),
    path('continueShopping/', views.continueShopping, name='continueShopping'),
    path('manageProducts', views.manageProducts, name='manageProducts'),
]