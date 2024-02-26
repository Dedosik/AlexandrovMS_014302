from django.urls import path, include
from accounts.api import views as api_views
from rest_framework import routers
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'profiles', api_views.ProfileViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token)
]