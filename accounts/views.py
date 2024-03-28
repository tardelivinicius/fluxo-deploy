from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from accounts.serializers import UserSerializer
from accounts.models import User


class AccountView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return User.objects.all()
