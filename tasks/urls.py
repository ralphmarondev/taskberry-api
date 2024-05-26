from django.urls import path 
from tasks import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
]
