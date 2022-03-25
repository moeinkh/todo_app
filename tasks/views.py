from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, ActiveForm
from django.urls import reverse

from django.http import JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    tasks = Task.objects.filter(user=request.user.id)
    form = TaskForm()       
    return render(request, 'tasks/home.html', {
        'tasks': tasks,
        'form': form,
        })

def taskajax(request):
    tasks = Task.objects.filter(user=request.user.id)
    data ={}
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
            return JsonResponse({ 'error': form.errors }, status=400)       
    return JsonResponse(data)       
            

def delete_task(request, id):
    tasks = Task.objects.filter(user=request.user.id)
    data = {}
    if request.method == 'POST':
        deleted = Task.objects.get(pk=id)
        deleted.delete()
        context = {
            'tasks': tasks
        }
        data = {'rendered_table_delete': render_to_string('tasks/task_list.html', context, request=request)}
        return JsonResponse(data)
    return JsonResponse(data)

def active_task(request, id):
    tasks = Task.objects.filter(user=request.user.id)
    data = {}
    if request.method == 'POST':
        # form = ActiveForm(request.POST)
        for ts in Task.objects.filter(user=request.user.id, id=id):
            if ts.active:
                ts.active = False
            else:
                ts.active = True
            ts.save()
            context = {
                'tasks': tasks
            }
            data = {'rendered_table_active': render_to_string('tasks/active_form.html', context, request=request)}
            return JsonResponse(data)
        else:
            return JsonResponse({ 'error': 'form.errors' }, status=400) 
    return JsonResponse(data)



