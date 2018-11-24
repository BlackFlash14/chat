from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import permissions
from .serializers import RoomSerializer
from .models import Room


class Rooms(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'data':  serializer.data  })


