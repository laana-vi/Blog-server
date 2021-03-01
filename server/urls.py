from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenRefreshView)
from blog.views import MyTokenObtainPairView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/', include('blog.urls', namespace='blog')),
    path('api/users/', include('users.urls', namespace='users')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
