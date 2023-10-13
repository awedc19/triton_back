from rest_framework import serializers
from .models import board
from django.contrib.auth.models import User, Group

class BoardSerializer(serializers.ModelSerializer):
    class Meta :
        model = board
        fields = '__all__'
        