from .models import Project 
from .serializers import ProjectSerializer , ProjectMemberSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.response import Response
from rest_framework import status
from projects.models import ProjectMember
from rest_framework import viewsets
from accounts.models import User
from rest_framework.exceptions import ValidationError

class ProjectList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        # Automatically assign the current user as the owner when creating a new project
        serializer.save(owner=self.request.user)

    



class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_update(self, serializer):
        # Update the owner field to the current user when updating a project
        serializer.save(owner=self.request.user)


    def destroy(self, request, *args, **kwargs):
        # Custom response for project deletion
        instance = self.get_object()

        # Check if the instance exists and has a valid ID
        if not instance:
            return Response({
                'status': 'error',
                'message': 'Project not found'
            }, status=status.HTTP_404_NOT_FOUND)

        # print(f"Deleting project with ID: {instance.id}")  # Debugging line to check the ID

        # Prepare the data to return in the response
        data = {
            'status': 'success',
            'message': 'Project deleted successfully',
            'id': instance.id
        }
        
        self.perform_destroy(instance)
        # Log the data for debugging
        print(data)
        
        return Response(data, status=status.HTTP_200_OK)  # Return with 200 OK






class ProjectMemberList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer




class ProjectMemberDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]  # Uncomment if you want to enforce token authentication
    permission_classes = [IsAuthenticated]
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer

    def perform_update(self, serializer):
        # Retrieve the user ID from the request data
        user_id = self.request.data.get('user')
        
        # print(user_id) # Debugging line to check the user ID
        if not user_id:
            raise ValidationError({"user": "User field is required."})
        try:
            # Get the user instance using the provided user ID
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({"user": "User with this ID does not exist."})

        # Check for unique constraint conflicts
        project = serializer.instance.project  # Get the current project
        if ProjectMember.objects.filter(project=project, user=user).exclude(id=serializer.instance.id).exists():
            raise ValidationError({"user": "This user is already assigned to this project."})

        # Save the updated user
        serializer.save(user=user)


    def destroy(self, request, *args, **kwargs):
        # Custom response for project deletion
        instance = self.get_object()

        # Check if the instance exists and has a valid ID
        if not instance:
            return Response({
                'status': 'error',
                'message': 'Project Member not found'
            }, status=status.HTTP_404_NOT_FOUND)

        # print(f"Deleting project with ID: {instance.id}")  # Debugging line to check the ID

        # Prepare the data to return in the response
        data = {
            'status': 'success',
            'message': 'Project Member deleted successfully',
            'id': instance.id
        }
        
        self.perform_destroy(instance)
        # Log the data for debugging
        print(data)
        
        return Response(data, status=status.HTTP_200_OK)  # Return with 200 OK