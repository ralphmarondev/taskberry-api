from django.db import models
from django.utils import timezone

class Task(models.Model):
  id=models.AutoField(primary_key=True)
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=255)
  date_created=models.DateTimeField(auto_now=True)
  is_deleted=models.BooleanField(default=False)
  
  def __str__(self):
    return self.title