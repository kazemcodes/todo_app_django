from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView 

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
    path('password-reset/', PasswordResetView.as_view(template_name='todo/password_reset.html',html_email_template_name='todo/password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='todo/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='todo/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='todo/password_reset_complete.html'),name='password_reset_complete'),
    path('profile/', views.MyProfile.as_view(),name='profile'),
]