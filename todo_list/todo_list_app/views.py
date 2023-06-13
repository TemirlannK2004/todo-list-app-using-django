from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import *

import datetime


from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

class Register(FormView):
    template_name="auth/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url= reverse_lazy('tasks')

    def form_valid(self, form):
        user= form.save()
        if user is not None:
            login(self.request,user)
        return super(Register,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register,self).get(*args,**kwargs)

        

    

class Login(LoginView):
    template_name="auth\login.html"
    fields='__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name='todo-list/task.html'
    context_object_name='tasks'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%A")
        context['formatted_date'] = formatted_date
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input    

        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    template_name='todo-list/task_detail.html'
    context_object_name='task'

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    template_name="todo-list/task_create.html"
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Create Form'
        return context 

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    template_name='todo-list/task_create.html'
    fields=['title','description','complete']
    success_url=reverse_lazy('tasks')
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Update Form'
        return context


class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    template_name='todo-list/task_delete.html'
    success_url=reverse_lazy('tasks')
   



    

