from django.shortcuts import render



# Create your views here.


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='resturant-home'),
    path('about/', views.about, name='resturant-about'),
    path('contact/', views.contact, name='resturant-contact'),
    path('menu/', views.menu, name='resturant-menu'),
    path('gallery/', views.gallery, name='resturant-gallery'),
    path('catering/', views.catering, name='resturant-catering'),
]

