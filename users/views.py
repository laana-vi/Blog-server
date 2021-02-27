from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.userobjects.all()
    serializer_class = CustomUserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class EditUser(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class DeleteUser(generics.RetrieveDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer