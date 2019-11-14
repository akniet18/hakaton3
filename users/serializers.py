from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from prapp.models import *
User = get_user_model()

class ratingser(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
	getRating = ratingser(many=True)
	rating = serializers.SerializerMethodField()
	
	class Meta:
		model = User
		fields = ('id', 'first_name', 'last_name', 'email', 
				'birth_date', 'avatar', 'location', 'gender', 
				'phone', 'work_place', 'rating', 'getRating')
		read_only_fields = ('getRating', 'rating')
	
	def rating(self):
		sum_r = 0
		rat = 0
		for i in self.rating_array:
			sum_r += i
			rat = sum_r / len(self.rating_array)
		return rat