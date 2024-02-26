from rest_framework import generics, viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from checks.models import *
from checks.api.serializers import *
from checks.business import check


class NewsViewSet(viewsets.ModelViewSet):
	queryset = News.objects.all()
	serializer_class = NewsSerializer


class CheckView(APIView):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticated]

	def put(self, request, format=None):
		serializer = CheckSerializer(data=request.data)
		if serializer.is_valid():
			news = serializer.save(user=request.user)
			predict = check.is_fake(news.title)
			news.is_fake = bool(predict)
			news.save()

			return Response({"fake": news.is_fake})

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
