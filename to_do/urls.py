from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_tasks, name='task_list'),
    path('viewtask/<int:task_id>/', views.get_task, name='task_view'),
    path('create/', views.create_task, name='task_create'),
    path('update/<int:task_id>/', views.update_task, name='task_update'),
    path('delete/<int:task_id>/', views.delete_task, name='task_delete'),
]