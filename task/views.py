from multiprocessing import context
from pyexpat import model
from queue import Empty
from urllib import response
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from .models import Task,SubTask
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from .form import TaskForm, UserRegisterForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def task_list(request):
    context ={}
    form =TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('task')  
    context['form']= form
    return render(request, "tasklist.html", context)
    # if request.method == "POST":
    #     form=TaskForm(request.POST or None)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(request ,'home')
    #     else:
    #         form=TaskForm()
    #         context={'form':form}
    #     return render(request,'tasklist.html',context)
    # else:
    #     form=TaskForm()
    #     return render(request, 'tasklist.html',{'form':form})

def task(request):
    tasks = Task.objects.all()
    # paginator=Paginator(task,2)
    # page_number=request.GET.get('page')
    # taskfinal=paginator.get_page(page_number)
    return render(request, "task.html",{'tasks':tasks})

def task_details(request,id):
    task = Task.objects.get(id=id)
    return render(request, "taskdetails.html",{'task':task})

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return HttpResponse('deleted')

def edit(request,id):
    task=Task.objects.get(id=id)
    task.task_name=request.POST.get('task_name')
    task.save()
    return HttpResponse('edit')



        



# def task(request):
#     form =Task.objects.all()
#     paginator=Paginator(form,2)
#     page_number=request.GET.get('page')
#     taskfinal=paginator.get_page(page_number)
#     return render (request, 'task.html',{'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task')
    else:
            
        form = AuthenticationForm()
    context ={'form':form}
    return render(request, "login.html", context)


    

