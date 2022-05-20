from django.urls import path

#from .views import posts,home,post,create_post,edit_post, delete_post

from . import views
app_name = 'posts'
urlpatterns = [
    path('', views.posts, name='posts_list'),
    path('my-posts', views.my_posts, name='my_posts_list'),
    path('create', views.create_post, name='post_create'),
    path('search', views.search, name='post_search'),
    path('<int:id>', views.post, name='post_detail'),
    path('edit/<int:id>', views.edit_post, name='post_edit'),
    path('delete/<int:id>', views.delete_post, name='post_delete'),
    path('comment/<int:id>', views.create_comment, name='comment_create'),
     path('delete-comment/<int:id>', views.delete_comment, name='comment_delete')
    
]


