from django.urls import path
from . import views
from .views import *



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>', PostByCategory.as_view(), name='category'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),
    path('tag/<str:slug>', get_tag, name='tag'),
    path('comment/<int:pk>/', views.AddComents.as_view(), name='add_comment'),
    path('search/', Search.as_view(), name='search'),
    path('add-post/', PostCreateView.as_view(), name='add_post'),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('author/<str:slug>', UserPostListView.as_view(), name='user-posts'),


]
