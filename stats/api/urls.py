from django.urls import path, include
from stats.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('v1/stats/', api_views.StatsView.as_view()),
]