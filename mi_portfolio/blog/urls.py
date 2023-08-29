from django.urls import path
from .views import posts_page, post_detail

app_name = 'blog'

urlpatterns = [
    path('', posts_page, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
]