from django.db import models
from django.utils import timezone 

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('low', 'Low'),
    ]

    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default='low')
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(max_length=50, default=timezone.now)
    end_time = models.DateTimeField(max_length=50, default=timezone.now)

    def __str__(self) -> str:
        return self.id
