from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'tasks/add_task.html')

def task_list(request):
    # Your view function logic here
    return render(request, 'tasks/task_list.html')  # Assuming you have a template