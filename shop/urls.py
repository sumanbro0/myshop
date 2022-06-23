# from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='shophome'),
    path('about/', views.about, name='Aboutus'),
    path('contact/', views.contact, name='Contactus'),
    path('tracker/', views.tracker, name='tracker'),
    path('search/', views.search, name='search'),
    path('products/<int:id>', views.products, name='products'),
    path('checkout/', views.checkout, name='checkout'),
]
