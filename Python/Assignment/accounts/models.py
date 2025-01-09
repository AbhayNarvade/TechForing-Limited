from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from .manager import UserManager
from django.utils.timezone import now

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Primary Key
    username = models.CharField(max_length=150, unique=True)  # Unique Username
    email = models.EmailField(unique=True)  # Unique Email
    password = models.CharField(max_length=128)  # Password
    first_name = models.CharField(max_length=30)  # First Name
    last_name = models.CharField(max_length=30)  # Last Name
    date_joined = models.DateTimeField(default=now)  # Date Joined

    # Custom User Manager
    objects = UserManager()

    # Use email for authentication instead of username
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
