from app.tasks.models.character import Character
from app.tasks.models.task import Task  # Make sure to use absolute import
from django.contrib import admin

@admin.register(Task)  # This decorator registers the model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description', 'created_at', 'is_completed', 'deleted_at', 'custom_fields')  # Fields to display
    list_filter = ('is_completed', 'created_at')  # Add filters
    search_fields = ('title', 'description')  # Add search functionality

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'health', 'strength')
    search_fields = ('user__username',)
