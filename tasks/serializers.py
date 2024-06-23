from rest_framework import routers, serializers, viewsets
from .models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # formatting the datetime fields
    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    end_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Task
        fields = ['id', 'description', 'priority', 'start_time', 'end_time']
        # fields = '__all__'
