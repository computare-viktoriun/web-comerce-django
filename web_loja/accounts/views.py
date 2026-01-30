
from accounts.models import BaseUser
from accounts.serializers import BaseUserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

# Create your views here.
class BaseUserViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
   #permission_classes = [IsAuthenticated]
