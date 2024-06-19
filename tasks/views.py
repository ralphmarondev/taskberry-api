from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import TaskSerializer
from .models import Task 
from http import HTTPStatus


@csrf_exempt
def tasks(request):
    if request.method == 'GET':
        return list_tasks(request)
    elif request.method == 'POST':
        return create_task(request)

def list_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False, status=HTTPStatus.OK)

def create_task(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
    return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=HTTPStatus.NOT_FOUND)

    if request.method == 'PUT':
        return update_task(request, task)
    elif request.method == 'DELETE':
        return delete_task(task)

def update_task(request, task):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(task, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=HTTPStatus.OK)
    return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

def delete_task(task):
    task.delete()
    return HttpResponse(status=HTTPStatus.NO_CONTENT)