<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
>>>>>>> 1636aaac2804ebd505568da83c1b62486485a03e
]