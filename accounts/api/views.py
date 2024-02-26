from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts.models import *
from accounts.api.serializers import *


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
