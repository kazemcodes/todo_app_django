from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.TaskList.as_view(template_name='todo/task_list.html'), name='tasks'),
    path('task/<int:pk>/', views.TaskDetail.as_view(template_name='todo/task_detail.html'), name='task'),
    path('task/create/', views.TaskCreate.as_view(template_name='todo/task_form.html'), name='task-create'),
    path('task/update/<int:pk>/', views.TaskUpdate.as_view(template_name='todo/task_form.html'),name='task-update'),
    path('task/delete/<int:pk>/', views.TaskDelete.as_view(template_name='todo/delete_task.html'),name='task-delete'),
    path('register/', views.RegisterUser.as_view(template_name='todo/register.html'), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('login/', views.MyLoginView.as_view(template_name='todo/login.html'), name='login'),
]