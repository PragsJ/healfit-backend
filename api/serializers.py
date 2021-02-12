from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Consultant, UserProfile, Blog, Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ConsultantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultant
        fields = ('id', 'name', 'org_name', 'yoe', 'mail_id')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'age', 'height', 'weight', 'avgcycledays', 'avgperioddays', 'lastperiod')


class BLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'publishdate', 'title', 'link', 'author', 'tags')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'Subject', 'StartTime', 'EndTime', 'IsAllDay')

