from django.urls import path
from .views import home, post_detail, admin, add_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('blog_admin/', admin, name='admin'),
    path('add_post/', add_post, name='add_post'),
    path('delete_post/', delete_post, name='delete_post'),
]
