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



# class OpencvView(viewsets.ModelViewSet):
# 	permission_classes = [permissions.AllowAny,]
# 	serializer_class = OpencvSer
# 	queryset = OpencvModel.objects.all()


class OpencvView(APIView):
	permission_classes = (permissions.AllowAny,)

	def post(self, request):
		s = OpencvSer(data = request.data)
		if s.is_valid():
			lists = s.validated_data['lists'].split(' ')
			
			a = OpencvModel.objects.all()
			for j in a:
				for i in lists:
					if j.name == i:
						j.attnedance = 'true'
						j.save()
					else:
						j.attnedance = 'false'
						j.save()
			return Response({'status': 'ok'})
		else:
			return Response(s.errors)
