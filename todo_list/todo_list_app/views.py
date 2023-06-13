from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from .models import *

import datetime


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions



class Login(LoginView):
    template_name="auth\login.html"
    fields='__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(ListView):
    model = Task
    template_name='todo-list/task.html'
    context_object_name='tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%A")
        context['formatted_date'] = formatted_date
        return context

    

    

class TaskDetail(DetailView):
    model = Task
    template_name='todo-list/task_detail.html'
    context_object_name='task'

class TaskCreate(CreateView):
    model=Task
    template_name="todo-list/task_create.html"
    fields="__all__"
    success_url=reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model=Task
    template_name='todo-list/task_create.html'
    fields="__all__"
    success_url=reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model=Task
    context_object_name='task'
    template_name='todo-list/task_delete.html'
    success_url=reverse_lazy('tasks')
   



    

