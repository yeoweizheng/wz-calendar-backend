from django.db import models
from django.contrib.auth.models import User

class ScheduleItem(models.Model):
    name = models.CharField(max_length=512)
    details = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    attributes = models.JSONField(null=True, blank=True)