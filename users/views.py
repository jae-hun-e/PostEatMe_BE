from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MiseListCreate(generics.ListCreateAPIView):
    queryset = Mise.objects.all()
    serializer_class = MiseSerializer


def test_html(req):
    return render(req, 'test.html')
