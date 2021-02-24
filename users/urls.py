from django.urls import path
from .views import CustomUserCreate, UsersList, UserDetail, EditUser, DeleteUser

app_name = 'users'

urlpatterns = [
    path('', UsersList.as_view(), name="users"),
    path('register', CustomUserCreate.as_view(), name="create_user"),
    path('user/edit/userdetail/<int:pk>/', UserDetail.as_view(), name='userdetail'),
    path('user/edit/<int:pk>/', EditUser.as_view(), name='edituser'),
    path('user/delete/<int:pk>/', DeleteUser.as_view(), name='deleteuser'),
]
