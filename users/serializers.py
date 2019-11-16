from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from prapp.models import *
User = get_user_model()


class userser(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('first_name', 'username', 'last_name', )

class RatingSerializer(serializers.ModelSerializer):
	author = userser()
	class Meta:
		model = Rating
		fields = '__all__'
		


class universer(serializers.ModelSerializer):
	class Meta:
		model = university
		fields = '__all__'


class insser(serializers.ModelSerializer):
	class Meta:
		model = institut
		fields = '__all__'


class cafser(serializers.ModelSerializer):
	institut = insser()
	class Meta:
		model = cafedra
		fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
	comment = RatingSerializer(many=True)
	Allrating = serializers.SerializerMethodField()
	university = universer(many=True)
	cafedra = cafser()
	
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email', 'cafedra',
				'birth_date', 'avatar', 'location', 'gender', 'job',
				'phone', 'work_place', 'Allrating', 'comment', 'university')
		read_only_fields = ('comment', 'Allrating')
	
	def Allrating(self):
		sum_r = 0
		rat = 0
		for i in self.rating_array:
			sum_r += i
			rat = sum_r / len(self.rating_array)
		return rat


class RegUsers(serializers.Serializer):
	username = serializers.CharField(max_length=15)
	email = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=20)


class LoginUsers(serializers.Serializer):
	username = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=20)


class searchUsers(serializers.Serializer):
	search_id = serializers.IntegerField()
