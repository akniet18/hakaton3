from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import (login as django_login,
                                 logout as django_logout)
User = get_user_model()


class ArticleView(generics.ListAPIView):
	permission_classes = [permissions.AllowAny,]
	queryset = User.objects.all()
	serializer_class = UserSerializer
	filter_backends = (filters.SearchFilter,)
	# filterset_fields = ['category', 'in_stock']
	search_fields = ['username', 'email', 'first_name', 'last_name']



class UserView(RetrieveUpdateDestroyAPIView):
	permission_classes = [permissions.AllowAny,]
	queryset = User.objects.all()
	serializer_class = UserSerializer



class Register(APIView):
	permission_classes = [permissions.AllowAny,]

	def post(self, request):
		s = RegUsers(data = request.data)
		if s.is_valid():
			username = s.validated_data['username']
			email = s.validated_data['email']
			password = s.validated_data['password']
			if User.objects.filter(username=username, email=email).exists():
				return Response({'status': 'User already exists'})
			else: 
				user = User.objects.create(
					username = username,
					email = email,
				)
				user.set_password(password)
				user.save()
				return Response({'status': 'ok'})
		else:
			return Response(s.errors)


class Login(APIView):
	permission_classes = [permissions.AllowAny,]

	def post(self, request):
		s = LoginUsers(data = request.data)
		if s.is_valid():
			username = s.validated_data['username']
			password = s.validated_data['password']

			if User.objects.filter(username=username).exists():
				u = User.objects.get(username=username)
				if u.check_password(password):
					django_login(request, u)
					if Token.objects.filter(user=u).exists():
						token = Token.objects.get(user=u)
					else:
						token = Token.objects.create(user=u)
					return Response({'token': token.key, 'uid': u.id, 'username': u.username})
				else:
					return Response({'status': 'username or password wrong'})
			else:
				return Response({'status': 'username or password wrong'})
		else:
			return Response(s.errors)


class SearchUserView(APIView):
	permission_classes = [permissions.AllowAny,]

	def post(self, request):
		s = searchUsers(data = request.data)
		if s.is_valid():
			search = s.validated_data['search_id']

			a = User.objects.filter(cafedra__institut_id = search)
			ser = UserSerializer(a, many=True)
			return Response({'users': ser.data})
		else:
			return Response(s.errors)



class InsView(generics.ListCreateAPIView):
	permission_classes = [permissions.AllowAny,]
	queryset = institut.objects.all()
	serializer_class = insser