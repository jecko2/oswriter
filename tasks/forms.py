from django import forms
from .models import Task, TaskDetail


class TaskForm(forms.ModelForm):
    # task_level = forms.ModelChoiceField(queryset=Task.TASK_LEVEL)
    # task_type = forms.ModelChoiceField(queryset=Task.TASK_TYPE)

    class Meta:
        model = Task
        fields = ['task_level', 'task_type', 'task_pages', ]
        widgets = {
            'task_level': forms.ModelChoiceField.widget(attrs={'class': 'task_level'}),
            'task_type': forms.ModelChoiceField.widget(attrs={'class': 'task_type'}),
            'task_pages': forms.IntegerField.widget(attrs={'class': 'task_pages'}),
        }
        labels = {
            'task_level': 'Select the level of the assignment',
            'task_type': ' Select the type of assignment',
            'task_pages': 'Selected number of pages',
        }


class TaskDetailForm(forms.ModelForm):
    class Meta:
        model = TaskDetail
        fields = ['task_title', 'task_description', 'end_date', 'task_files', 'task_images',
                  'task_resources', ]
        widget = {
            'task_title': forms.TextInput(attrs={
                'class': 'task-title',
                'placeholder': 'enter the task title'
            }),
            'task_description': forms.Textarea(attrs={
                'class': 'task-description',
                'placeholder': 'Describe your task',
            }),
            'end_date': forms.DateTimeInput(attrs={
                'class': 'task-end-date',
                'placeholder': 'Duration for the task'
            }),
            'task_files': forms.FileInput(attrs={
                'class': 'task-files',
                'placeholder': 'files'
            }),
            'task_resources': forms.URLInput(attrs={
                'class': 'task-links',
                'placeholder': 'Additional links'
            }),
        }
        label = {
            'task_title': 'Task Title',
            'task_description': 'Task Description',
            'end_date': 'End Date',
            'task_files': 'Task Files',
            'task_images': 'Task Images',
            'task_resources': 'Task Resources',
        }

