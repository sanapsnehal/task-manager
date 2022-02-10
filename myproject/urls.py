"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from task.views import delete, home, login_request,task_list,task,task_details,edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view=home,name="home"),
    path('login',view=login_request,name="login"),
    path('tasklist',view=task_list,name="tasklist"),
    path('task',view=task,name="task"),
    path('taskdetails/<int:id>',view=task_details,name="taskdetails"),
    path('delete/<int:id>',view=delete),
    path('edit/<int:id>',view=edit,name="edit")


]
