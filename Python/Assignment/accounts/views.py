from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register(request):
    # Initialize serializer with data from the request
    serializer = UserSerializer(data=request.data)
    
    # Check if the provided data is valid
    if serializer.is_valid():
        # Save the new user instance
        user = serializer.save()
        # Create the token for the new user
        token, created = Token.objects.get_or_create(user=user)
        # print(token)
        data = {
            "status": 'User created successfully',
            "token": token.key
        }
        # Return a response with the created data and 201 status
        return Response(data, status=status.HTTP_201_CREATED)
    
    # If the data is invalid, return the errors with a 400 status
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
