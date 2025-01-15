from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Task
import json


def get_all_tasks(request):
    tasks = Task.objects.all().values()
    return JsonResponse(list(tasks), safe=False)


def get_task(request, task_id):
    task = get_object_or_404(Task, task_id=task_id)
    return JsonResponse({
        "task_id": task.task_id,
        "title": task.title,
        "completed": task.completed,
        "created_at": task.created_at,
    })


@csrf_exempt
def create_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title", "")
        completed = data.get("completed", False)
        task = Task.objects.create(title=title, completed=completed)
        return JsonResponse({
            "message": "Task created successfully",
            "task_id": task.task_id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at,
        })


@csrf_exempt
def update_task(request, task_id):
    if request.method == "PUT":
        task = get_object_or_404(Task, task_id=task_id)
        data = json.loads(request.body)
        task.title = data.get("title", task.title)
        task.completed = data.get("completed", task.completed)
        task.save()
        return JsonResponse({
            "message": "Task updated successfully",
            "task_id": task.task_id,
            "title": task.title,
            "completed": task.completed,
            "created_at": task.created_at,
        })


@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, task_id=task_id)
        task.delete()
        return JsonResponse({"message": "Task deleted successfully"})
