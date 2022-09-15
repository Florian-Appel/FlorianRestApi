
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo.views import ToDoViewSet

"""
Code from django rest framework site
"""

router = routers.DefaultRouter()
router.register(r'todos', ToDoViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('index/', ToDoViewSet),
]
