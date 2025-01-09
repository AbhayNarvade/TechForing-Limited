from django.db import models
from accounts.models import User
import uuid

def generate_short_uuid():
    return str(uuid.uuid4()).split('-')[0]  # Generates the first segment of the UUID

class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=generate_short_uuid, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member'),
    ]
    id = models.CharField(primary_key=True, max_length=8, default=generate_short_uuid, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_memberships')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('project', 'user')  # Ensures a user cannot be added to the same project multiple times

    def __str__(self):
        return f"{self.user.username} - {self.role} in {self.project.name}"
