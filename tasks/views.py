from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializer
from .models import Task

@csrf_exempt
def tasks(request):
    if request.method == 'GET':
        return list_tasks(request)
    elif request.method == 'POST':
        return create_task(request)

def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)

def create_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        return update_task(request, task)
    elif request.method == 'DELETE':
        return delete_task(task)

def update_task(request, task):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)  # Changed status to 200
    return JsonResponse(serializer.errors, status=400)

def delete_task(task):
    task.delete()
    return HttpResponse(status=204)
