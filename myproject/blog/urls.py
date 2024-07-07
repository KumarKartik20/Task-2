from django.urls import path
from .views import create_post, my_posts, list_posts

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('my_posts/', my_posts, name='my_posts'),
    path('posts/', list_posts, name='list_posts'),
]
