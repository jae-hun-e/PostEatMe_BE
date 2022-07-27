from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def get_post(req):
    if req.method == 'POST':
        id = req.POST.get('id')
