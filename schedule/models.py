from django.db import models
from django.contrib.auth.models import User

class ScheduleItem(models.Model):
    name = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    done = models.BooleanField(default=False)