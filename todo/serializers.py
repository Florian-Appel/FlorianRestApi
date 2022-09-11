from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ToDo

"""
Da "User" was komplexeres ist, wir in der folgenden klasse gesagt, was genau wir aus "User" haben wollen.
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']

"""
Erstellung einer REST-API (django-rest-framework.org)
-> Wenn wir einen GET request machen, wird hier gesagt welche felder wir bekommen.
(time_passed ist nur ein test)
"""

class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ToDo
        fields = ['id','title', 'description', 'chreated_at', 'time_passed']