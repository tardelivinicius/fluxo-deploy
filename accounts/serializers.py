from rest_framework import serializers
from django.utils.translation import gettext as _
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'full_name',
            'picture',
        ]

    def load_queryset(self, user):
        return User.objects.filter(pk=user.id)