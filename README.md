# ProjectFlow API

A backend project management API built with Django and Django REST Framework.

## Features
- User registration
- JWT authentication
- Project CRUD
- Task CRUD
- User-owned data access
- Basic automated API tests

## Tech Stack
- Python
- Django
- Django REST Framework
- Simple JWT
- SQLite (development)

## API Endpoints

### Authentication
- POST `/api/auth/register/`
- POST `/api/auth/login/`
- POST `/api/auth/refresh/`

### Projects
- GET `/api/projects/`
- POST `/api/projects/`
- GET `/api/projects/<id>/`
- PUT `/api/projects/<id>/`
- DELETE `/api/projects/<id>/`

### Tasks
- GET `/api/tasks/`
- POST `/api/tasks/`
- GET `/api/tasks/<id>/`
- PUT `/api/tasks/<id>/`
- DELETE `/api/tasks/<id>/`

## Running the Project

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver