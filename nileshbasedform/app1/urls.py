from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
   
    path("", views.home),
    path("about", views.about),
    path("services", views.services),
    path("contact", views.contact),
    
   
   
]