from rest_framework import serializers
from accounts.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["username", "email", "first_name", "last_name"]


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)

	class Meta:
		model = Profile
		fields = '__all__'