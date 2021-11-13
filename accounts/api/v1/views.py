from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import logout

@api_view(['GET'])
def logout_view(request):
    request.user.auth_token.delete()
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def signup(request):
    data = {'data': '', 'status': ''}
    serialized_user = UserSerializer(data=request.data)
    if serialized_user.is_valid():
        serialized_user.save()
        data['data'] = {'message': 'New user Created', 'user': serialized_user.data,
                        'token': Token.objects.get(user__username=serialized_user.data.get('username')).key}
        data['status'] = status.HTTP_200_OK
    else:
        data['data'] = serialized_user.errors
        data['status'] = status.HTTP_400_BAD_REQUEST
    return Response(**data)