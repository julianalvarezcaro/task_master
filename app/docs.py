from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse
)
from .serializers import TaskSerializer

# Reusable examples
TASK_EXAMPLES = [
    OpenApiExample(
        'Minimal Task',
        value={"title": "Read documentation"},
        summary='Required fields only'
    ),
    OpenApiExample(
        'Full Task',
        value={
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "custom_fields": {"priority": "high"}
        },
        summary='All available fields'
    )
]

# Schema definitions
TASK_SCHEMAS = {
    'create': {
        'examples': TASK_EXAMPLES,
        'responses': {
            201: TaskSerializer,
            400: OpenApiResponse(
                description="Validation Error",
                examples=[
                    OpenApiExample(
                        'Error Example',
                        value={"title": ["This field is required."]}
                    )
                ]
            )
        }
    },
    'list': {
        'parameters': [
            OpenApiParameter(
                name='user_id',
                type=int,
                location=OpenApiParameter.PATH,
                description='ID of the user whose tasks to retrieve'
            )
        ],
        'examples': [
            OpenApiExample(
                'Success Response',
                value=[{
                    "id": 1,
                    "title": "Sample task",
                    "user": 1
                }],
                response_only=True
            )
        ]
    },
    'complete': {
        'operation_id': 'task_complete',
        'description': 'Mark a specific task as completed',
        'parameters': [
            OpenApiParameter(
                name='task_id',
                type=int,
                location=OpenApiParameter.PATH,
                description='ID of the task to complete'
            )
        ],
        'responses': {
            200: OpenApiResponse(
                description='Task marked as completed',
                examples=[
                    OpenApiExample(
                        'Success',
                        value={"status": "Task marked as completed"}
                    )
                ]
            ),
            403: OpenApiResponse(
                description='Forbidden - Not task owner/admin',
                examples=[
                    OpenApiExample(
                        'Error',
                        value={"detail": "You can only complete your own tasks"}
                    )
                ]
            ),
            404: OpenApiResponse(
                description='Task not found'
            )
        }
    }
}