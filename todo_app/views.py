from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import TaskList, Task

#test2

def index(request):

    tasks = Task.objects.filter(task_list=request.user.id).all()

    content = {'tasks': tasks}

    return render(request, 'index.html', content)




def cs_logout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/register.html', context)