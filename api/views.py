from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, ConsultantSerializer, UserProfileSerializer, BLogSerializer, EventSerializer
from .models import Consultant, UserProfile, Blog, Event


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConsultantViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows consultants to be viewed or edited.
    """
    queryset = Consultant.objects.all()
    serializer_class = ConsultantSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
            API endpoint that allows userProfile to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
            API endpoint that allows list of BLogs to be viewed or edited.
    """
    queryset = Blog.objects.all().order_by('publishdate').reverse()
    serializer_class = BLogSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
                API endpoint that allows list of Events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('StartTime')
    serializer_class = EventSerializer
