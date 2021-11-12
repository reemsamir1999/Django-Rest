from django.urls import path
from .views import *


urlpatterns =[
    path('hello',hello, name='hello'),
    path('getmovies',getmovies, name='getmovies'),
    path('postmovie',postmovie, name='postmovie'),
    path('getmovie/<int:pk>/',getmovie, name='getmovie'),
    path('deletemovie/<int:pk>/',deletemovie, name='deletemovie'),
    path('updatemovie/<int:pk>/', updatemovie, name='updatemovie'),
]