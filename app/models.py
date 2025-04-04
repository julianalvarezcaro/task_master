from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Fixed Core Fields (Always present)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    # Flexible Custom Fields (Stored as JSON)
    custom_fields = models.JSONField(
        default=dict,
        blank=True,
        encoder=None,  # Uses Django's default JSON encoder
        decoder=None
    )

    class Meta:
        indexes = [
            models.Index(fields=['user', 'is_completed']),  # Speeds up common queries
        ]
        ordering = ['-created_at']  # New tasks first by default

    def __str__(self):
        return f"{self.title} (User: {self.user.username})"
