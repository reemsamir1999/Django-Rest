from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import *

urlpatterns = [
  path('signup', signup, name='signup'),
  path('login', obtain_auth_token,  name='login' ),
  path('logout', logout,  name='logout' ),
]
