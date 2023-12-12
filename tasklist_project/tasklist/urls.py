from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskListAPIView, CreateUserAPIView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('users/', CreateUserAPIView.as_view(), name='create-user'),
]