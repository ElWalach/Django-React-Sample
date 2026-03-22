from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class CreateUserView(generics.CreateAPIView):
    queryset= User.objects.all()     #zeby nie bylo takiego samego usera
    serializer_class= UserSerializer  #info co trzeba zeby zrobic takiego usera
    permission_classes= [AllowAny]  #kazdy ma mozliwosc zrobic nowego usera
