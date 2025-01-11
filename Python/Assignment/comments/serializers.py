from rest_framework import serializers
from .models import Comment
from accounts.models import User
from tasks.models import Task
from tasks.serializers import TaskSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False) # Use the `__str__` method of the User model
    task =  TaskSerializer(read_only=True)  # Use the `__str__` method of the Task model

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'task', 'created_at']
        read_only_fields = ['id', 'created_at']
