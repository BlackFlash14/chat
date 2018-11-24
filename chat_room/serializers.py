from rest_framework import serializers
from .models import Room
from django.contrib.auth.models import User

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ("user", "text", "date")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class RoomSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    invited = UserSerializer(many=True)
    class Meta:
        model = Room
        fields = ("creator", "invited", "date")
