from django.shortcuts import render
from .serializers import *
from rest_framework import generics


class MemoListCreate(generics.ListCreateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer


def del_data(req, name):
    # record = Memo.objects.all()
    record = Memo.objects.filter(name=name)
    # print(record)
    record.delete()
    return render('test.html')


# def memo_log(req, name):
#     record = Memo.objects.filter(name=name)
