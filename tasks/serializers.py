from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    assignee = serializers.ReadOnlyField(source='assignee.username')
    project_name = serializers.ReadOnlyField(source='project.name')

    class Meta:
        model = Task
        fields = [
            'id',
            'project',
            'project_name',
            'assignee',
            'title',
            'description',
            'status',
            'priority',
            'due_date',
            'created_at',
        ]