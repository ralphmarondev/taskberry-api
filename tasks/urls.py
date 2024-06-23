from django.urls import path, include
from .views import TaskViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
urlpatterns = [
    # path('tasks/', views.tasks, name='task')
    path('', include(router.urls))
]
