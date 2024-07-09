
from django.shortcuts import render, redirect
from .models import ToDo

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add_task(request):
    if request.method == 'POST':
        task = request.POST['task']
        ToDo.objects.create(task=task)
        return redirect('index')
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    ToDo.objects.get(id=task_id).delete()
    return redirect('index')
            