from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from backend.user_profile.models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'date_joined')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ( 'user', 'id', 'picture', 'about', 'avatar', 'customer_categories')


