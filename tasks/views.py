from django.shortcuts import render
from .models import Task
from .forms import TaskForm
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