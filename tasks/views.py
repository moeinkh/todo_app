from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, ActiveForm
from django.urls import reverse
from django.core import serializers

from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    tasks = Task.objects.filter(user=request.user.id).order_by('-created')
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.title = form.cleaned_data['title']
            task.user = request.user
            task.save()
            context = {
                'tasks': tasks,
            }
            data = {'rendered_table': render_to_string('tasks/task_list.html', context, request=request)}
            return JsonResponse(data)
        else:
            return JsonResponse({'error': form.errors }, status=400) 
    else:
        form = TaskForm()  
        return render(request, 'tasks/home.html', {
            'tasks': tasks,
            'form': form,
        })

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('/')

def active_task(request, id):
    task = Task.objects.get(id=id)
    task.active = False
    print(task)
    task.save()
    return redirect('/')


