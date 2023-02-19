from django.shortcuts import render
from .models import Dives
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DivesSerializer


# Create your views here.
class DivesViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Dives.objects.all()
    # The serializer class for serializing output
    serializer_class = DivesSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Could be [permissions.IsAuthenticated]

