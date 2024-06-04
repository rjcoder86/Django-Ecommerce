from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, CustomTokenObtainPairSerializer

User = get_user_model()
LOGIN_TIME_IN_DAYS = 14
LOGIN_TIME = LOGIN_TIME_IN_DAYS * 24 * 3600


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as err:
            return Response({'error': "Provide Invalid Details"}, status=400)
        except IntegrityError as err:
            return Response({'error': "User Already Exist"}, status=403)


class CustomLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response()
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            response.set_cookie('refresh_token', serializer.validated_data.get(
                'refresh', None), httponly=True, secure=True, max_age=LOGIN_TIME, samesite='None')
            response.set_cookie('token', serializer.validated_data.get(
                'refresh', None), httponly=True, domain="new.keywordio.com", secure=True, max_age=LOGIN_TIME, samesite=None)
            response.data = serializer.validated_data
            response.status_code = status.HTTP_200_OK
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token', None)
        response = Response()
        try:
            if refresh_token is None:
                raise ValueError("Refresh token not found.")

            response.set_cookie('refresh_token', httponly=True, max_age=1)
            response.status_code = status.HTTP_200_OK
            response.data = {"message": "User Logged out successfully"}

        except Exception as e:
            response.data = {'error': str(e)}
            response.status_code = status.HTTP_400_BAD_REQUEST
        return response
