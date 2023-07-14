from django.urls import path
from . import views

urlpatterns = [
        path("", views.home),
        path("posts/", views.view_post),
        path("categories/", views.view_category , name='category'),
        path("authors/",views.view_authors),
        path('categories/category_details/<int:id>', views.view_category_detail, name='category_details'),
        path('posts/post_details/<int:id>', views.view_post_detail, name='post_details'),
        ]