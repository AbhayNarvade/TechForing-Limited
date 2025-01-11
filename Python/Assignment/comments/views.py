from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
