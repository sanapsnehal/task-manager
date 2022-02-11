from asyncio import Task
from django.contrib import admin
from .models import SubTask, Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_name','status','owner_id']
    list_filter = ['status']

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['sub_task','task_id']
