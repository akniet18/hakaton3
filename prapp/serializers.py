from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = '__all__'
		read_only_fields = ('author', )

	def update(self, instance, validated_data):
		instance.rating = validated_data['rating']
		instance.comment = validated_data['comment']
		instance.save()
		return instance