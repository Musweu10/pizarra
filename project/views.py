from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Project


@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user)
    ctx = {'projects': projects}
    return render(request, 'project/projects.html', ctx)


@login_required
def project_detail(request,pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    ctx = {'project': project}
    return render(request, 'project/project_details.html', ctx)
    
@login_required
def add_project(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Project.objects.create(
                name=name, description=description, created_by=request.user)
            return redirect('/projects/')
        else:
            print('No name specified')

    return render(request, 'project/add_project.html')


@login_required
def edit_project(request,pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            project.name = name
            project.description = description
            project.save()

            return redirect('/projects/')
        
    ctx = {'project': project}
    return render(request, 'project/edit_project.html', ctx)
    

@login_required
def delete_project(request,pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    project.delete()

    return redirect('/projects/')