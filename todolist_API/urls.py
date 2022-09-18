
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from todo.views import ToDoViewSet
from todo.views import index

"""
Code from django rest framework site
"""

router = routers.DefaultRouter()
router.register(r'todos', ToDoViewSet)

from todo.views import index, login_view
from todo.views import registration_view
from todo.views import logout_view

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login_view),
    path('registration/', registration_view),
    path('logout/', logout_view),
]
