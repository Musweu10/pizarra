from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from project.models import Project
from task.models import Task
from todolist.models import Todolist


@login_required
def add_task(request, project_id, todolist_id):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=todolist_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Task.objects.create(
                project=project, todolist=todolist, name=name,
                description=description, created_by=request.user)

        return redirect(f'/projects/project-item/{project_id}/todo-item/{todolist_id}/')

    return render(request, 'task/add_task.html')
