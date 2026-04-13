from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project


class ProjectAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='testpass123')
        response = self.client.post('/api/auth/login/', {
            'username': 'owner',
            'password': 'testpass123'
        }, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_project(self):
        response = self.client.post('/api/projects/', {
            'name': 'Test Project',
            'description': 'Project description'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(Project.objects.first().owner, self.user)