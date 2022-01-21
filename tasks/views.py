from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, ActiveForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else: 
        form = TaskForm()       
        return render(request, 'tasks/home.html', {
            'tasks': tasks,
            'form': form,
            })

def delete_task(request, id):
    deleted = Task.objects.get(pk=id)
    deleted.delete()
    return redirect('task:home')

def active_task(request, id):
    task = Task.objects.get(pk=id)
    if request.method == 'POST':
        form = ActiveForm(request.POST)
        if form.is_valid():
            if task.active:
                task.active = False
                task.save()
                return redirect('task:home')
            else:
                task.active = True
                task.save()
                return redirect('task:home')
    else:
        form = ActiveForm()
        return redirect('task:home')



