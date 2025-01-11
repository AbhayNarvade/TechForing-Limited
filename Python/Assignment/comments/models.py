from django.db import models
from accounts.models import User
from tasks.models import Task
import uuid
# Create your models here.
def generate_short_uuid():
    return str(uuid.uuid4()).split('-')[0]  # Generates the first segment of the UUID

class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=8, default=generate_short_uuid, editable=False)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.task.title}"