from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from todo.models import Task
from django.contrib import messages



def home(request):
    return render(request,'home.html')    


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        messages.success(self.request, "Task updated successfully")
        return super().form_valid(form)
    
class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks')
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task Create successfully")
        return super().form_valid(form)