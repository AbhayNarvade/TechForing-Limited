

```markdown
# Project Name - Project Management Tool

This is a backend API developed for **TechForing Limited**, which is building a project management tool to allow teams to collaborate on projects. The API manages users, projects, tasks, and comments, and is designed to be consumed by both the front-end web application and mobile application.

## Project Structure

- **accounts/**: User authentication and management
- **projects/**: Project-related models and views
- **tasks/**: Task management functionality
- **comments/**: Commenting system
- **taskmanageproject/**: Main Django project configuration

## API Endpoints

- **/api/accounts/**: User authentication
- **/api/projects/**: Project management
- **/api/tasks/**: Task management
- **/api/comments/**: Commenting system

### Users
- **Register User** (POST `/api/users/register/`): Create a new user.
- **Login User** (POST `/api/users/login/`): Authenticate a user and return a token.
- **Get User Details** (GET `/api/users/{id}/`): Retrieve details of a specific user.
- **Update User** (PUT/PATCH `/api/users/{id}/`): Update user details.
- **Delete User** (DELETE `/api/users/{id}/`): Delete a user account.

### Projects
- **List Projects** (GET `/api/projects/`): Retrieve a list of all projects.
- **Create Project** (POST `/api/projects/`): Create a new project.
- **Retrieve Project** (GET `/api/projects/{id}/`): Retrieve details of a specific project.
- **Update Project** (PUT/PATCH `/api/projects/{id}/`): Update project details.
- **Delete Project** (DELETE `/api/projects/{id}/`): Delete a project.

### Task
- **List Tasks** (GET `/api/projects/{project_id}/tasks/`): Retrieve a list of all tasks in a project.
- **Create Task** (POST `/api/projects/{project_id}/tasks/`): Create a new task in a project.
- **Retrieve Task** (GET `/api/tasks/{id}/`): Retrieve details of a specific task.
- **Update Task** (PUT/PATCH `/api/tasks/{id}/`): Update task details.
- **Delete Task** (DELETE `/api/tasks/{id}/`): Delete a task.

### Comments
- **List Comments** (GET `/api/tasks/{task_id}/comments/`): Retrieve a list of all comments on a task.
- **Create Comment** (POST `/api/tasks/{task_id}/comments/`): Create a new comment on a task.
- **Retrieve Comment** (GET `/api/comments/{id}/`): Retrieve details of a specific comment.
- **Update Comment** (PUT/PATCH `/api/comments/{id}/`): Update comment details.
- **Delete Comment** (DELETE `/api/comments/{id}/`): Delete a comment.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AbhayNarvade/TechForing-Limited.git
cd project-name
```

### 2. Set Up a Virtual Environment

Make sure Python is installed on your system, then create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Make sure your database settings are correctly configured in `settings.py`. Then, run the migrations:

```bash
python manage.py migrate
```

### 5. Create a Superuser

Create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

### 6. Run the Server

Run the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the app.

## Requirements

- **asgiref**==3.8.1
- **Django**==5.1.4
- **djangorestframework**==3.15.2
- **sqlparse**==0.5.3

## Acknowledgements

The backend for this API was developed as part of the project for **TechForing Limited** to manage users, projects, tasks, and comments for their project management tool.

