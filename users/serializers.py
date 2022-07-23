from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone')


class MiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mise  # 직렬화 할 목록
        fields = '__all__'