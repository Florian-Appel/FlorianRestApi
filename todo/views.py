from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ToDoSerializer
from .models import ToDo

"""
Code from django rest framework site
"""

class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('-chreated_at')
    serializer_class = ToDoSerializer
    permission_classes = [] # permissions.IsAuthenticated