from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from tasks.models import Task

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('task:home')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })            

def profile(request):
    user = get_object_or_404(User, pk=request.user.id)
    count_tasks = Task.objects.filter(user=request.user.id).count()
    count_active = Task.objects.filter(user=request.user.id, active=True).count()
    return render(request, 'registration/profile.html', {
        'user': user,
        'count_tasks': count_tasks,
        'count_active': count_active,
    }) 