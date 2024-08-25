from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.auth import UserSerializer

@api_view(['POST'])
@csrf_exempt
def register(request):
    print('request: ', request)
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    username = email.split('@')[0]  # Simple username generation

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already registered."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@csrf_exempt
def login(request):
    email = request.data.get('email')
    print('email: ', email)
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=email.split('@')[0], password=password)
    if user is not None:
        auth_login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def logout(request):
    print('email: ', request)
    auth_logout(request)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
