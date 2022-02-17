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
from .form import SubForm, TaskForm, UserRegisterForm
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def task_list(request):
    context ={}
    print(request.POST)
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

def subtask(request):
    context={}
    form =SubForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return redirect('')  
    context['form']= form
    return render(request, "subtask.html", context)


def task(request):
    if request.user.is_authenticated:
        # task_list = Task.objects.all().order_by('-id')
        task_list = Task.objects.filter(owner_id = request.user)
        paginator=Paginator(task_list,4)  
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request, "task.html", {'page_obj':page_obj,'user':request.user})
    else:
        return HttpResponseRedirect('/login')

def task_details(request,id):
    task=Task.objects.get(id=id)
    subtask = SubTask.objects.filter(task_id = id)
    stform =SubForm(request.POST or None)
    if stform.is_valid():
        stform.save()
    return render(request, "taskdetails.html",{'task':task, 'subtask':subtask,'stform':stform})

    # form=SubForm(instance=subtask)
    # if request.method == 'POST':
    #    form=SubForm(request.POST, instance=subtask)
    #    if form.is_valid():
    #       form.save() 

def delete(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return HttpResponse('deleted')

def edit(request,id):
    task=Task.objects.get(id=id)
    form=TaskForm(instance=task)
    if request.method == 'POST':
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
           form.save()
           return redirect('/')
    context={'form':form}

    return render(request,"tasklist.html",context)




        



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


    

