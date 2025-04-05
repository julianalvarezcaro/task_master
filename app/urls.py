from app.tasks.views.character_views import CharacterDetailView
from app.tasks.views.task_views import (
    TaskCompleteView,
    TaskCreateView,
    UserTaskListView
)
from app.tasks.views.user_views import RegisterView
from django.urls import path

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('tasks/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:task_id>/complete/', TaskCompleteView.as_view(), name='task-complete'),
    path('users/<int:user_id>/character/', CharacterDetailView.as_view(), name='character-detail'),
    path('users/<int:user_id>/tasks/', UserTaskListView.as_view(), name='user-tasks'),
]
