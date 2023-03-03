from django.contrib import admin
from django.urls import path, include
from home import views




urlpatterns = [
    path('', views.home, name = 'home'),
    path('index.html', views.home, name = 'home'),
    path('contact.html', views.contact, name = 'contact'),
    path('about.html', views.about, name = 'about'),
    
    

     
]
