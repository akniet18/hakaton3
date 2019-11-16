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
from django.contrib.auth import get_user_model
from rest_framework import filters
User = get_user_model()



class Rat(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated,]
	# permission_classes = [permissions.AllowAny,]
	authentication_classes = [TokenAuthentication]

	serializer_class = RatingSerializer
	queryset = Rating.objects.all()
	filter_backends = (filters.SearchFilter,)
	search_fields = ['id', 'rating', 'comment']
	filter_fields = ('id', 'rating', 'comment')

	def create(self, request):
		s = RatingSerializer(data=request.data)
		if s.is_valid():
			print(s.validated_data, request.user)
			rat = s.validated_data['rating']
			users = s.validated_data['user']
			Rating.objects.create(
				rating=rat,
				comment=s.validated_data['comment'], 
				author=request.user,
				user=users
			)
			users.rating_array.append(rat)
			users.save()
			return Response({'status': "created"})
		else:
			return Response(s.errors)