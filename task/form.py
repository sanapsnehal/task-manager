from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Task,SubTask
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields ='__all__'

class SubForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields  = ['sub_task']