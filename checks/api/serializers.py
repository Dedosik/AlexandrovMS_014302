from rest_framework import serializers
from checks.models import *


class NewsSerializer(serializers.ModelSerializer):

	class Meta:
		model = News
		fields = ['user', 'title', 'body', 'created', 'is_fake']


class CheckSerializer(serializers.ModelSerializer):

	class Meta:
		model = News
		fields = ['title', 'body']
