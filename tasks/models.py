from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('low', 'Low'),
    ]

    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default='low')
    start_time = models.DateTimeField(max_length=50)
    end_time = models.DateTimeField(max_length=50)

    def __str__(self) -> str:
        return self.title
