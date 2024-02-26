from django.urls import path, include
from checks.api import views as api_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'news', api_views.NewsViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/check/', api_views.CheckView.as_view())
]