from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, TaskCreationForm
from .models import TaskList, Task, TaskList

#test2

def index(request):

    tasks = Task.objects.filter(task_list=request.user.id).all()

    context={}
    context['tasks'] = tasks

    form = TaskCreationForm()

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task_list_instance = TaskList.objects.get(pk=request.user.id)
            task.task_list = task_list_instance
            task.save()
            return redirect('/')
        else:
            form = TaskCreationForm()

    context['form'] = form

    return render(request, 'index.html', context)




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