from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.exceptions import NotFound

# Create your views here.
class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



class CommentList (generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        if task_id:
            queryset = Comment.objects.filter(task_id=task_id)
            if not queryset.exists():
                raise NotFound(f"No Comments found for task_id {task_id}")
            return queryset
        raise NotFound("Task ID is required.")


    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)  # Fetch the Project object
        serializer.save(task=task)