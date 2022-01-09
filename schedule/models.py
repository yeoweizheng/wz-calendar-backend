from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ScheduleItem(models.Model):
    name = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    done = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, null=True, blank=True)
