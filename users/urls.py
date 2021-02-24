from django.urls import path
from .views import CustomUserCreate, UsersList

app_name = 'users'

urlpatterns = [
    path('', UsersList.as_view(), name="users"),
    path('register', CustomUserCreate.as_view(), name="create_user"),
]
