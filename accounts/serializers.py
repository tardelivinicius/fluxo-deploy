from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'picture',
        ]

    def load_queryset(self, user):
        return User.objects.filter(pk=user.id)
