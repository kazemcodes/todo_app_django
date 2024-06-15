from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.TaskList.as_view(template_name='todo/task_list.html'), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(template_name='todo/task_detail.html'), name='task'),
   
    path('task/update/<int:pk>/', views.TaskUpdate.as_view(template_name='todo/task_form.html'),name='task-update'),
]