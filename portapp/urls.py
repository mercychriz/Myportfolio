from django.urls import path 
from . import views

urlpatterns=[
    #path('', views.home, name='home'),
    path('',views.contact_form),
    #path('contact/', views.contact_form, name='contact_form'),
]