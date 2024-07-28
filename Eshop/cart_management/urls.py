from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('openCart', views.openCart, name='openCart'),
    path('removeFromCart', views.removeFromCart, name='removeFromCart'),

]