from rest_framework import serializers
from .models import Project, ProjectMember
from accounts.models import User
from accounts.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)  # Nested UserSerializer for the owner
    members = serializers.StringRelatedField(many=True ,read_only=True)  # Nested serializer for members

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'members', 'created_at']

        


class ProjectMemberSerializer(serializers.ModelSerializer):

    class Meta:
        project = ProjectSerializer(read_only=True)  # Display the project name
        user = UserSerializer(read_only=True)  # Nested UserSerializer to display user details
        model = ProjectMember
        fields = ['id', 'project', 'user', 'role']
