
from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities_list, name='list'),
    path('new-communitie/', views.communities_new, name="new"),
    path('<slug:slug>', views.Community_page, name="page")
]