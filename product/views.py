from django.shortcuts import render
from rest_framework.response import Response
from .models import board
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import BoardSerializer

# Create your views here.

class BoardListAPI(APIView):
    def get(self, request):
        queryest = board.object.all()
        print(queryest)
        serializer = BoardSerializer(queryest, many=True)
        return Response(serializer.data)
    
    
