from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from api import serializers
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
