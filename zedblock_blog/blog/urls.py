from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('blog_admin/', admin, name='admin'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('add_edit_post/', add_edit_post, name='add_edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
]
