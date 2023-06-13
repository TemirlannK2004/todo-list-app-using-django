from django import views
from django.urls import path,include
from .views import *
from rest_framework import routers




urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(),name='task'),
    path('create_task/',TaskCreate.as_view(),name='create_task'),
    path('update_task/<int:pk>/',TaskUpdate.as_view(),name='update_task'),
    path('delete_task/<int:pk>/',TaskDelete.as_view(),name='delete_task'),
    path('login/',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),

     path('logout/',LogoutView.as_view(next_page='login'),name='logout'),

]
