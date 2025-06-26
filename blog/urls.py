from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("posts/", views.post_list,name="post_list"),
    path("post_details/<int:post_id>/", views.post_details,name="post_details")
]
