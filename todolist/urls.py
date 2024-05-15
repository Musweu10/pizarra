from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('add-todo/', views.add_todo, name="add-todo"),
    path('todo-item/<uuid:pk>/', views.todolist, name="todolist"),
    path('edit-todo/<uuid:pk>/', views.edit_todo, name="edit-todo"),
    path('delete-todo/<uuid:pk>/', views.delete_todo, name="delete-todo")
]
