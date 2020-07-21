from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.user_profile.models import Profile
from backend.user_profile.serializers import UserSerializer, ProfileSerializer

User = get_user_model()


class UserView(APIView):
    """ Получить пользователя """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ser = UserSerializer(User.objects.get(id=request.user.id))
        return Response(ser.data)


class ProfileView(APIView):
    """ Получить профиль пользователя """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        ser = ProfileSerializer(Profile.objects.get(id=request.user.id))
        return Response(ser.data)
