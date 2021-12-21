from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('post_comment/', views.post_comment, name='postComment'),

    path('', views.blog_home, name='BLogHome'),
    path('<str:slug>/', views.blog_post, name='BLogPost'),


]
