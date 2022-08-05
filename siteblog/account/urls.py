from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login', ),
    path('profile/', profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
]