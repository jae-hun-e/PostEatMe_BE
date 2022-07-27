from django.shortcuts import render
from .serializers import *
from rest_framework import generics


class MemoListCreate(generics.ListCreateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
