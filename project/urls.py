from django.urls import path
from .import views

app_name = 'project'

urlpatterns = [
    path('', views.projects, name="projects"),    
    path('project-details/<uuid:pk>/', views.project_detail, name="project-details"),
    path('add-project/', views.add_project, name="add-project"),
    path('edit-project/<uuid:pk>/', views.edit_project, name="edit-project"),
    path('delete-project/<uuid:pk>/', views.delete_project, name="delete-project"), 
]

# 1:47:02 mins
