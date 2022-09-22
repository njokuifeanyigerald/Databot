# from re import I
from django.urls import path
from .views import (RegisterAPIView,LoginAPIView, LogoutView, 
        updatePassword, updateUser, getUserProfile, getUsers,
        getUserById, deleteUser)


# # sc
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path("update_password/", updatePassword, name="updateUser"),
    path('update/<str:pk>/', updateUser, name='user-profile-update'),

    path('profile/', getUserProfile, name="user-profile"), 
    path('users/', getUsers, name="users"),    
    path('user/<str:pk>', getUserById, name="user"),    
    path('delete_user/<str:pk>', deleteUser, name="delete-User"),    
]