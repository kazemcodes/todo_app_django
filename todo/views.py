from django.shortcuts import render
from django.views.generic.list import ListView

from todo.models import Task



def home(request):
    return render(request,'home.html')    


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'