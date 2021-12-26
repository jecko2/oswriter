from django.shortcuts import render, redirect
from .forms import TaskForm, TaskDetailForm
from django.shortcuts import reverse
from .models import Task, TaskDetail
from django.views import generic
from django.contrib import messages

class TaskFormView(generic.CreateView):
    form_class = TaskForm
    template_name = 'task/task_form.html'
    
    def get_success_url(self):
        return reverse('task:task_detail')
def taskViewForm(request):
    if request.method == 'GET':
        form = TaskForm()
        context = {'form': form}
        return render(request, 'tasks/task_form.html', context)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form_user = form.save(commit=False)
            form_user.client = request.user
            form.save()
            return redirect('task:task_detail')
    return render(request, 'tasks/task_form.html', context)


def task_detail(request):
    if request.method == 'POST':
        form = TaskDetailForm(request.POST, request.FILES)
        if form.is_valid():
            form_task = form.save(commit=False)
            form_task.task = Task.objects.get('task_type').latest()
            form.save()
            return redirect('payment:payment_method')
    else:
        form = TaskDetailForm()
    return render(request, 'tasks/task_detail_form.html', {'form': form})
