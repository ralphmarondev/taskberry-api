from rest_framework import routers, serializers, viewsets
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # formatting the date
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created_at']
