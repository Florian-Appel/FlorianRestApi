from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ToDo

"""
Erstellung einer REST-API (django-rest-framework.org)
"""

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id','title', 'description', 'chreated_at'] # user