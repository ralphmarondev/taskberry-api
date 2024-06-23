from django.db import models
from django.utils import timezone 

class Task(models.Model):
    description = models.CharField(max_length=255, default="")
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.description
