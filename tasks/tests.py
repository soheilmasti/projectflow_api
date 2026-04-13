from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from projects.models import Project
from .models import Task


class TaskAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='testpass123')
        response = self.client.post('/api/auth/login/', {
            'username': 'owner',
            'password': 'testpass123'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.project = Project.objects.create(
            owner=self.user,
            name='Project One',
            description='Test project'
        )

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            'project': self.project.id,
            'title': 'Test Task',
            'description': 'Task description',
            'status': 'todo',
            'priority': 'medium'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().project, self.project)