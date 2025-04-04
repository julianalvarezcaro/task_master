from app.models import Task
from app.serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import generics, permissions

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated access

class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Auto-set the user to the current logged-in user
        serializer.save(user=self.request.user)
