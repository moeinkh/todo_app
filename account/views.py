from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login

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