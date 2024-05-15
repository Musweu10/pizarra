from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Todolist
from project.models import Project


@login_required
def todolist(request, project_id, pk):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)
    ctx = {
        'project': project,
        'todolist': todolist
    }
    return render(request, 'todolist/todolist.html', ctx)


@login_required
def add_todo(request, project_id):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Todolist.objects.create(
                project=project, name=name,
                description=description, created_by=request.user)

            return redirect(f'/projects/project-details/{project_id}/')

    ctx = {'project': project}
    return render(request, 'todolist/add_todo.html', ctx)


def edit_todo(request, project_id, pk):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)
    todolist = Todolist.objects.filter(project=project).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            todolist.name = name
            todolist.description = description
            todolist.save()

            return redirect(f'/projects/project-item/{project_id}/todo-item/{pk}/')
    ctx = {
        'project': project,
        'todolist': todolist
    }
    return render(request, 'todolist/edit_todo.html', ctx)


def delete_todo(request, project_id, pk):
    project = Project.objects.filter(
        created_by=request.user).get(pk=project_id)
    todo_item = Todolist.objects.filter(project=project).get(pk=pk)
    todo_item.delete()

    return redirect(f'/projects/project-details/{project_id}')