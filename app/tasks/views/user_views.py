from app.serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """
    Handles user registration
    - AllowAny permission: No auth required
    - Uses UserSerializer for validation
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
