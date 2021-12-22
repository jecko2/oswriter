from django.contrib import admin
from .models import Task, TaskDetail


class TaskAdmin(admin.ModelAdmin):
    list_display = ['client', 'task_level', 'task_type', 'task_pages', ]
    list_filter = ['client', 'task_level', 'task_type']
    fieldsets = (
        ('TASK SUMMARY VIEW', {
            'fields': ('client', 'task_level', 'task_type', 'task_pages',),
        }),
    )


class TaskDetailAdmin(admin.ModelAdmin):
    list_display = ['task', 'task_title', 'end_date']
    list_filter = ['task', 'task_title', 'start_date', 'end_date', ]
    fieldsets = (
        ('TASK DETAIL VIEW', {
            'fields': (
                'task', 'task_title', 'task_description', 'end_date',
                'task_resources', 'task_files', 'task_images'),
        }),
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskDetail, TaskDetailAdmin)

