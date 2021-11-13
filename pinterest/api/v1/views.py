from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pinterest.models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission


class CanDeleteMovie(BasePermission):
 def has_permission(self, request, view):
    return request.user.groups.filter(name="Delete Movie").exists()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hello(request):
    data = {'message' : 'Hello'}
    return Response(data=data)


@api_view(['GET'])
def getmovies(request):
    movies = Movie.objects.all()
    serialized_movies = MovieSerializer(instance= movies, many=True)
    return Response(data=serialized_movies.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def postmovie(request):
    serialized_movie = MovieSerializer(data=request.data)
    if serialized_movie.is_valid():
        serialized_movie.save()
    else:
        return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)
    data = {'message':'New Movie is added',
            'data':serialized_movie.data}
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getmovie(request,pk):
    movie = Movie.objects.filter(pk=pk)
    if movie.exists:
        pass
    else:
        return Response(data={'message':'Sorry Movie is no found!'}, status=status.HTTP_400_BAD_REQUEST)
    serialized_movie = MovieSerializer(instance=movie, many=True)
    return Response(data=serialized_movie.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([CanDeleteMovie])
def deletemovie(request,pk):
    try:
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(data={'message': 'Movie deleted successful'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','PATCH'])
def updatemovie(request,pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'PUT':
        serialized_movie = MovieSerializer(instance=movie,data=request.data)
    if request.method == 'PATCH':
        serialized_movie = MovieSerializer(instance=movie,data=request.data, partial=True)
    if serialized_movie.is_valid():
        serialized_movie.save()
        data = {'message': 'Movie is updated',
                'data': serialized_movie.data}
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(data=serialized_movie.errors, status=status.HTTP_400_BAD_REQUEST)















