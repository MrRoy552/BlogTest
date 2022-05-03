from django.shortcuts import render
from .serializers import*
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from .pagination import*



class blogView(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=blogSerializer
    http_method_names=['post','get','put']
    permission_classes=[IsAuthenticated]
    pagination_class = CustomPagination


class userRegister(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserRegistrationSerializer
    http_method_names=['post','get']
    permission_classes=[AllowAny,]


