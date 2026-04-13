from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if project.owner != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You cannot create tasks for a project you do not own.")
        serializer.save()


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project__owner=self.request.user)