from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import Game

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],     password = validated_data['password']  ,first_name=validated_data['first_name'],  last_name=validated_data['last_name'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name', 'last_name','is_staff','is_active','date_joined')

# Game serializer
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model= Game
        fields='__all__'

# class GameStartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Game
#         fields=('game_id','string')
    
#     def create(self, validated_data):
#         game = Game.objects.create_user(validated_data['game_id'], string=validated_data['string'])
#         return game

