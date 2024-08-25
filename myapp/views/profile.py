from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..serializers.auth import UserSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    user = request.user
    print('user: ', user)
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def set_cookie(request):
    response = Response({"message": "Cookie set"})
    response.set_cookie('test_cookie', 'test_value', samesite='None', secure=False)  # Adjust secure based on your setup
    return response
