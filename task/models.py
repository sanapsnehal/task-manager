from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = (
    ("1", "open"),
    ("2", "close"),
    )
    task_name=models.CharField(max_length=100)
    status=models.CharField(max_length=120,choices=STATUS_CHOICES,default=1)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    staff_status=models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

class SubTask(models.Model):
    sub_task=models.CharField(max_length=120)
    task_id=models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_task

        

class RequestLog(models.Model):
    name = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name