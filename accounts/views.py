from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializers import UserSerializer
from rest_framework.decorators import action
from accounts.models import User

class AccountView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return User.objects.all()
