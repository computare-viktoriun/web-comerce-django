from django.urls import path,include
from accounts.views import BaseUserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', BaseUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]