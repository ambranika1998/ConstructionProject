from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from construction.constants import USER_TYPE_JSON
from construction.models import User, ConstructionSite, Trellis, Job, JobUser


class UserSerializer(ModelSerializer):
    user_type_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'user_type', 'user_type_name']
        extra_kwargs = {'id': {'read_only': True}}

    def get_user_type_name(self, obj):
        return USER_TYPE_JSON[obj.user_type]


class ConstructionSiteSerializer(ModelSerializer):
    class Meta:
        model = ConstructionSite
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': True}}


class TrellisSerializer(ModelSerializer):
    class Meta:
        model = Trellis
        fields = ['id', 'construction_site', 'number', 'base_area', 'top_area', 'total_area']
        extra_kwargs = {'id': {'read_only': True}}


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'trellis', 'position', 'start_date', 'end_date']
        extra_kwargs = {'id': {'read_only': True}}


class JobUserSerializer(ModelSerializer):
    class Meta:
        model = JobUser
        fields = ['id', 'job', 'user', 'start_date', 'end_date']
        extra_kwargs = {'id': {'read_only': True}}
