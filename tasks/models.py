from django.db import models
from users.models import CustomUser
from django.urls import reverse


class Task(models.Model):
    TASK_LEVEL = (
        ('HIGH SCHOOL', 'High School'),
        ('COLLEGE', 'College'),
        ('UNDERGRADUATE', 'Undergraduate'),
        ('MASTERS', 'Masters')
    )
    TASK_TYPE = (
        ('ESSAY', 'Essay'),
        ('REPORT', 'Report'),
        ('CASE STUDY', 'Case Study'),
    )
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_level = models.CharField(max_length=100, choices=TASK_LEVEL)
    task_type = models.CharField(max_length=100, choices=TASK_TYPE)
    task_pages = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.task_type}"


class TaskDetail(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=250)
    task_description = models.TextField()
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=False)
    task_files = models.FileField(upload_to='media/files/', blank=True, null=True)
    task_images = models.ImageField(upload_to='media/images/', blank=True, null=True)
    task_resources = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f'{self.task.task_type}'


