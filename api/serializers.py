from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Consultant, UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('id', 'name', 'org_name', 'yoe', 'mail_id')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'age', 'height', 'weight', 'avgcycledays', 'avgperioddays', 'lastperiod')
