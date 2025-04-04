# Import necessary modules from DRF and Django
from app.models import Task
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    # Explicit password field configuration:
    password = serializers.CharField(
        write_only=True,       # Never included in serialized responses
        required=True,         # Must be provided during registration
        validators=[validate_password]  # Enforces Django's password validation rules
    )
    
    class Meta:
        model = User  # Uses Django's built-in User model
        fields = ('username', 'password', 'email')  # Fields to include in serialization
        # Optional: Add field-level validations
        extra_kwargs = {
            'email': {'required': False}  # Makes email optional
        }

    def create(self, validated_data):
        # Creates and returns a new User instance using Django's create_user helper:
        # - Properly hashes the password automatically
        # - Handles username normalization
        user = User.objects.create_user(
            username=validated_data['username'],  # Required field
            password=validated_data['password'],  # Will be hashed
            email=validated_data.get('email', '')  # Optional field (empty string default)
        )
        return user  # Returns the created user instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'is_completed', 'created_at', 'deleted_at', 'custom_fields']
        read_only_fields = ['id', 'user', 'created_at', 'deleted_at']  # Auto-set fields
        extra_kwargs = {
            'custom_fields': {'required': False}  # Makes this field optional
        }
