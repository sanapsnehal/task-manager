from asyncio import Task
from django.contrib import admin
from .models import SubTask, Task, RequestLog
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','task_name','status','owner_id','staff_status']
    list_filter = ['status','staff_status']

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['sub_task','task_id']

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['name','timestamp']
