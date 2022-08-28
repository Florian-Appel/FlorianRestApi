from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers

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

    """
    Funtion dafür das ein POST request ausgeführt werden kann:
    """

    def create(self, request):
        todo = ToDo.objects.create(title=request.POST.get('title', ''), description= request.POST.get('description', ''), user= request.user,)
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')