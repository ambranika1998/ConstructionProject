from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from construction.constants import USER_TYPE_CHOICES
from construction.models import User


class UserSerializer(ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'user_type']
        extra_kwargs = {'id': {'read_only': True}}

    def get_user_type(self, obj):
        return USER_TYPE_CHOICES[obj.user_type]
