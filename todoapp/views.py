from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
        return redirect('todo_list')  # <-- fix here

    tasks = Task.objects.all()
    return render(request, 'todo.html', {'tasks': tasks})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.is_done = not task.is_done
        task.save()
    return redirect('todo_list')  # <-- fix here

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
    return redirect('todo_list')  # <-- fix here
