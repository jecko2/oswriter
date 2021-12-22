from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.taskViewForm, name='task-view'),
    path('detail/', views.task_detail, name='task_detail'),
]
