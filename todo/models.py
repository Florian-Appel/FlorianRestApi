from turtle import title
from django.db import models
import datetime
from django.conf import settings
from datetime import date

class ToDo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    chreated_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    """
    Man kann eine Funtion in das Model packen, so das es dann auch in der API erscheint. (siehe serializer.py)
    """

    def time_passed(self):
        today = date.today()
        delta = today - self.chreated_at
        return delta.days