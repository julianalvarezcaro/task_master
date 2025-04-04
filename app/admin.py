from app.models import Task  # Make sure to use absolute import
from django.contrib import admin

@admin.register(Task)  # This decorator registers the model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'created_at', 'is_completed', 'deleted_at', 'custom_fields')  # Fields to display
    list_filter = ('is_completed', 'created_at')  # Add filters
    search_fields = ('title', 'description')  # Add search functionality
