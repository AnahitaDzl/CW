from django.urls import path
from . import views

urlpatterns = [
        path("", views.home),
        path("posts/", views.view_post),
        ]