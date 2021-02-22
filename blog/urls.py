from .views import PostList, CategoriesList, PostDetail, CreatePost, AdminPostDetail, EditPost, DeletePost
from django.urls import path

app_name="blog"


urlpatterns = [
    path('posts/', PostList.as_view(), name='listpost'),
    path('posts/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('categories/', CategoriesList.as_view(), name='categories'),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]