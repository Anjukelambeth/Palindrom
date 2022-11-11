from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializer import UserSerializer,GameSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
import json
from .models import Game
import string
import random
# from django.shortcuts import redirect

class HelloView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		serializer = UserSerializer(request.user)
		print(serializer.data)
		name=serializer.data['username']
		content = {'message': 'Hello,'+name,}
		return Response(content)

# @api_view(['GET'])
# def allUser(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)
#adminside  
class AllUser(APIView):
	permission_classes = (IsAdminUser, )

	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
#adminside	
class DeleteUser(APIView):
	permission_classes = (IsAdminUser, )

	def post(self, request,pk):
		user = User.objects.get(id=pk)
		user.delete()
		content = {'message': 'Deleted,'+user.username,}
		return Response(content,status=status.HTTP_202_ACCEPTED)
	
#adminside
class EditUser(APIView):
	permission_classes = (IsAdminUser, )

	def post(self, request,pk):
		user = User.objects.get(id=pk)
		userData =  UserSerializer(instance=user, data=request.data, partial=True)
		if userData.is_valid():
			userData.save()
			return Response(userData.data, status=status.HTTP_200_OK)

#adminside
class NewUserAdd(APIView):
	permission_classes = (IsAdminUser, )
	def post(self,request ):
		print('POST', request.body)
		body = request.body.decode('utf-8')
		body = json.loads(body)
		first_name=body['first_name']
		last_name=body['last_name']
		email=body['email']
		username=body['username']
		password=body['password'] 
		user = User.objects.create_user(email=email,username=username,password=password ,first_name=first_name,last_name=last_name)
		user.save()
		content = {'message': 'New UserCreated,'}
		return Response (content, status=status.HTTP_200_OK)

class GameStart(APIView):
	permission_classes = (IsAuthenticated, )
	def post(self, request):
		try:
			listing = Game.objects.latest('game_id')
			# print(listing.game_id)
			if listing:
				game_id=listing.game_id+1
				# print(00000)
				# print(game_id)
				user=request.user
				game_string=""
				new_game=Game.objects.create_game(game_id=game_id,game_string=game_string,user=user)
				new_game.save()
				g_id=str(game_id)
				content = {'message': 'New Game_Id Created,'+g_id}
				return Response (content, status=status.HTTP_200_OK)
		except Game.DoesNotExist:
			listing = None
			game_id=1
			game_string=""
			user=request.user
			new_game=Game.objects.create_game(game_id=game_id,game_string=game_string,user=user)
			new_game.save()
			print(game_id)
			print(999999)
			g_id=str(game_id)
			content = {'message': 'New Game_Id Created,'+g_id}
			return Response (content, status=status.HTTP_200_OK)
		
class GetBoard(APIView):
	permission_classes = (IsAuthenticated, )
	def get(self,request):
		game_start=Game.objects.filter(user=request.user).latest('game_id')
		game_str=game_start.game_string
		size=len(game_str)
		print(size)
		print(game_str)
	
		if size !=6:
			game_str = game_str+''.join(random.choices(string.ascii_lowercase, k=1))
			new_game=Game.objects.create_game(game_id=game_start.game_id,game_string=game_str,user=request.user)
			new_game.save()
			print(909)
			print(new_game.game_string)
			return Response (game_str, status=status.HTTP_200_OK)

		else:
			if game_str == game_str[::-1]:
				content = {'message': 'This is a palindrome.' }
				return Response (content, status=status.HTTP_200_OK)
			else:
				content = {'message': 'This is not a palindrome.' }
				return Response (content, status=status.HTTP_200_OK)
	
	def post(self,request):
		game_start=Game.objects.filter(user=request.user).latest('game_id')
		game_str=game_start.game_string
		size=len(game_str)
		print(size)
		print(game_str)
	
		if size !=6:
			data=request.data
			print('hai')
			print(data)
			print('hello')
			new_char=data["game_string"]
			game_str = game_str+new_char
			new_game=Game.objects.create_game(game_id=game_start.game_id,game_string=game_str,user=request.user)
			new_game.save()
			print(909)
			print(new_game.game_string)
			return Response (game_str, status=status.HTTP_200_OK)
		else:
			if game_str == game_str[::-1]:
				content = {'message': 'This is a palindrome.' }
				return Response (content, status=status.HTTP_200_OK)
			else:
				content = {'message': 'This is not a palindrome.' }
				return Response (content, status=status.HTTP_200_OK)

class GameList(APIView):
	permission_classes = (IsAuthenticated, )
	def get(self,request):
		lists=Game.objects.all().filter(user=request.user)
		serializer = GameSerializer(lists, many=True)
		return Response(serializer.data)

#adim-side
class GameListAll(APIView):
	permission_classes = (IsAdminUser, )
	def get(self,request):
		lists=Game.objects.all()
		serializer = GameSerializer(lists, many=True)
		return Response(serializer.data)

#user-side		
class EditAccount(APIView):
	permission_classes = (IsAuthenticated, )
	def post(self, request):
		user = User.objects.get(id=request.user.id)
		userData =  UserSerializer(instance=user, data=request.data, partial=True)
		if userData.is_valid():
			userData.save()
			return Response(userData.data, status=status.HTTP_200_OK)

class DeleteAccount(APIView):
	permission_classes = (IsAuthenticated, )
	def post(self, request):
		user = User.objects.get(id=request.user.id)
		user.delete()
		content = {'message': 'Deleted,'+user.username,}
		return Response(content,status=status.HTTP_202_ACCEPTED)