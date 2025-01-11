from rest_framework import serializers
from projects.models import Project, ProjectMember
from accounts.models import User
from accounts.serializers import UserSerializer
from .models import Task
from projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
    # Allow assigning by user ID
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    # Readable representation of the assigned user
    assigned_to_display = serializers.SerializerMethodField()
    project = ProjectSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'assigned_to','assigned_to_display', 'project', 'created_at', 'due_date']
        read_only_fields = ['id', 'created_at']

    def get_assigned_to_display(self, obj):
        """Returns a string representation of the assigned user."""
        return str(obj.assigned_to) if obj.assigned_to else None