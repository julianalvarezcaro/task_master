from app.views import RegisterView, TaskCreateView
from django.urls import path

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskCreateView.as_view(), name='task-create')
]
