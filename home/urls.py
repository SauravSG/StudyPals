from django.urls import path

from . import views

urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
  
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'), 
  
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),

    path('update-user/', views.updateUser, name='update-user'),
    path('topics/', views.topicsPage, name='topics'),
    path('activity/', views.activityPage, name='activity'),
    # Define the room/ URL pattern here
]
"""'room/'<str:pk>'' - on opening the room link, when we append the primary key (pk) as query parameter that will open the 1st entry i.e. Room1. here primary key basically indicates the particular room.id. Depending upon the pk we will be taken to that id page and get the particular room details."""
