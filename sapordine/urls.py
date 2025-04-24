from django.contrib import admin  
from django.urls import path  
from sapordine import views  
urlpatterns =[
       path('',views.show),
       path('contact/', views.contact_view, name='contact'),
]