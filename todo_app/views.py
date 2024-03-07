from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, TaskCreationForm
from .models import Task, TaskList, SortingType

#test2




@login_required(login_url='login/')
def index(request):

    if len(TaskList.objects.filter(user=request.user)) == 0:
        tasklist = TaskList(user=request.user, title=request.user)
        tasklist.save()
        task_list_instance = TaskList.objects.get(user=request.user)
        sortype = SortingType(task_list=task_list_instance)
        sortype.save()
        return redirect('index')

    task_list_instance = TaskList.objects.get(user=request.user)
    sort_by_instance = SortingType.objects.get(task_list=task_list_instance)

    if sort_by_instance.sort_by == SortingType.SORT_BY_CHOICES[0][0]:
        tasks = Task.objects.filter(task_list=task_list_instance).order_by('-id').all()
    elif sort_by_instance.sort_by == SortingType.SORT_BY_CHOICES[1][0]:
        tasks = Task.objects.filter(task_list=task_list_instance).order_by('date_added').all()
    elif sort_by_instance.sort_by == SortingType.SORT_BY_CHOICES[2][0]:
        tasks = Task.objects.filter(task_list=task_list_instance).order_by('-color_filter').all()


    context = {}
    context['tasks'] = tasks

    form = TaskCreationForm()

    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task_list_instance = TaskList.objects.get(user=request.user)
            task.task_list = task_list_instance
            task.save()
            return redirect('/')
        else:
            form = TaskCreationForm()


    context['form'] = form
    context['sort_by'] = sort_by_instance.sort_by

    return render(request, 'index.html', context)

def change_color_filter(request, id):
    COLOR_CHOICES = ('default-filter-color', 'color-filter-red', 'color-filter-orange',
                     'color-filter-green', 'color-filter-cyan', 'color-filter-blue',
                     'color-filter-purple'
                     )

    task_list = TaskList.objects.get(user=request.user)
    task = Task.objects.get(id=id, task_list=task_list)

    index =[i for i,e in enumerate(COLOR_CHOICES) if e == task.color_filter]
    index = int(index[0])
    if index == 6:
        task.color_filter = COLOR_CHOICES[0]
    else:
        task.color_filter = COLOR_CHOICES[index+1]
    task.save()
    return redirect('/')

def change_sorting(request):
    task_list_instance = TaskList.objects.get(user=request.user)
    sort_by_instance = SortingType.objects.get(task_list=task_list_instance)

    if sort_by_instance.sort_by == SortingType.SORT_BY_CHOICES[0][0]:
        sort_by_instance.sort_by = SortingType.SORT_BY_CHOICES[1][0]
        sort_by_instance.save()
    elif sort_by_instance.sort_by == SortingType.SORT_BY_CHOICES[1][0]:
        sort_by_instance.sort_by = SortingType.SORT_BY_CHOICES[2][0]
        sort_by_instance.save()
    elif sort_by_instance.sort_by == SortingType.SORT_BY_CHOICES[2][0]:
        sort_by_instance.sort_by = SortingType.SORT_BY_CHOICES[0][0]
        sort_by_instance.save()

    return redirect('index')


def delete(request, id):
    task_list_instance = TaskList.objects.get(user=request.user)
    Task.objects.filter(id=id, task_list=task_list_instance).delete()
    return redirect('/')


def update_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        is_completed = request.POST.get('is_completed')
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Task not found', 'temp': task_id})

        task.completed = not task.completed
        task.save()

        return JsonResponse({'status': 'success true', 'id': task.id, 'completed': task.completed})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

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