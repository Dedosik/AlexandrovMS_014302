from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Profile
from checks.models import News


class StatsView(APIView):
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAdminUser]

	def get(self, request, format=None):
		news_stats = News.get_stats()
		subscriptions_stats = Profile.get_stats()
		response = {
			"news": news_stats,
			"subscriptions": subscriptions_stats
		}
		return Response(response)

