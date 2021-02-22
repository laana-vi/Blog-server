from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenRefreshView)
from blog.views import MyTokenObtainPairView

urlpatterns = [
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls', namespace='blog')),
    path('api/users/', include('users.urls', namespace='users')),

]
