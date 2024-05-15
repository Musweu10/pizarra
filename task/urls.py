from django.urls import path
from. import  views


app_name = 'task'

urlpatterns = [
    path('add-task/', views.add_task, name='add-task'),
]
