from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from .serializers import ToDoSerializer
from .models import ToDo

@login_required(login_url='/login/')

def index(request):
    return render(request, 'index.html')


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
        todo = ToDo.objects.create(title=request.POST.get('title', ''), description= request.POST.get('description', ''), user= self.request.user)
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')


def login_view(request):
    """
    This is the view for the Login Page
    """
    redirect = request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get('redirect'))
        else:
            return render(request, 'auth/login.html', {'wrongPassword': True, 'redirect': redirect})
    return render(request, 'auth/login.html', {'redirect': redirect})


def registration_view(request):
    """
    This is the view for the Register Page
    """
    redirect = request.GET.get('next')
    if request.method == 'POST':
        try:
            
            user = User.objects.create_user(username=request.POST.get('register-username'), password=request.POST.get('register-password'))
            user.save()
            return HttpResponseRedirect(request.POST.get('redirect'))
        except:
            return render(request, 'auth/registration.html', {'redirect': redirect, 'error': 'Benutzer konnte nicht angelegt werden'})
    return render(request, 'auth/registration.html', {'redirect': redirect})


def logout_view(request):
    """
    This is the view for the Logout
    """
    logout(request)
    return HttpResponseRedirect('/login')