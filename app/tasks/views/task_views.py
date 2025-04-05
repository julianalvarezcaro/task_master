from app.docs import TASK_SCHEMAS
from app.tasks.models.task import Task
from app.serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(**TASK_SCHEMAS['create'])
    def perform_create(self, serializer):
        """Auto-assigns the current user to new tasks"""
        serializer.save(user=self.request.user)


class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(**TASK_SCHEMAS['list'])
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        
        # Security check: Non-admins can only view their own tasks
        if not self.request.user.is_staff and self.request.user.id != int(user_id):
            raise PermissionDenied(
                {"detail": "You do not have permission to view these tasks"}
            )
            
        return Task.objects.filter(user_id=user_id)


class TaskCompleteView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    
    @extend_schema(**TASK_SCHEMAS['complete'])
    def patch(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=self.kwargs['task_id'])
        serializer = TaskSerializer(task, data={'is_completed': True}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        task.user.character.gain_experience(10)
        return Response(serializer.data)
