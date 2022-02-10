from asyncio import Task
from django.contrib import admin
from .models import SubTask, Task
# Register your models here.
admin.site.register(Task)
admin.site.register(SubTask)

