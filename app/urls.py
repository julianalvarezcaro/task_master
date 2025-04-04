from app.views import RegisterView, TaskCompleteView, TaskCreateView, UserTaskListView
from django.urls import path

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskCreateView.as_view(), name='task-create'),
    path('users/<int:user_id>/tasks/', UserTaskListView.as_view(), name='user-tasks'),
    path('api/tasks/<int:task_id>/complete/', TaskCompleteView.as_view(), name='task-complete'),
]
