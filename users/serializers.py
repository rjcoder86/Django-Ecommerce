from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials')

        refresh = RefreshToken.for_user(user)
        return {
            'email': user.email,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email','password', 'phone']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            phone=validated_data.get('phone', None)
        )
        return user
