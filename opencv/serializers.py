from rest_framework import serializers
from .models import *


class OpencvSer(serializers.Serializer):
	lists = serializers.CharField()