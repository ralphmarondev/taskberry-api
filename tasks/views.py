# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from .serializers import TaskSerializer
# from .models import Task

# @csrf_exempt
# def tasks(request):
#     if request.method == 'GET':
#         return list_tasks(request)
#     elif request.method == 'POST':
#         return create_task(request)


# def list_tasks(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many=True)
#     return JsonResponse(serializer.data, safe=False)

# def create_task(request):
#     data = JsonResponse().parse(request)
#     serializer = TaskSerializer(data  = data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data, status=201)
#     return JsonResponse(serializer.errors, status=400)

from rest_framework import viewsets
from .models import Task 
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
