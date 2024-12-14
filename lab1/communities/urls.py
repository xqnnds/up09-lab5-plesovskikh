from django.contrib import admin
from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name='list'),
    path('<slug:slug>', views.Community_page, name="page")
]