from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def del_user(req):
    record = User.objects.all()
    record.delete()
    return render('test.html')
