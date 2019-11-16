from rest_framework import serializers
from .models import *


class OpencvSer(serializers.ModelSerializer):
	class Meta:
		model = OpencvModel
		fields = '__all__'