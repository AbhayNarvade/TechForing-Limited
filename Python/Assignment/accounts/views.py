from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework import generics




@api_view(['POST'])
def register(request):
    # Initialize serializer with data from the request
    serializer = UserSerializer(data=request.data)
    
    # Check if the provided data is valid
    if serializer.is_valid():
        # Save the new user instance
        serializer.save()
        
        data = {
            "status": 'User created successfully',
        }
        # Return a response with the created data and 201 status
        return Response(data, status=status.HTTP_201_CREATED)
    
    # If the data is invalid, return the errors with a 400 status
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def login(request):
    # Get username and password from the request body
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Check if the user exists
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise AuthenticationFailed("Invalid username or password")
    
    # Check if the password is correct
    if not user.check_password(password):
        raise AuthenticationFailed("Invalid username or password")
    
    # Generate token if the login is successful
    token, created = Token.objects.get_or_create(user=user)
    
    data = {
        "status": "User logged in successfully",
        "token": token.key
    }

    return Response(data, status=status.HTTP_200_OK)



class UsersViewSetList(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)  
        data = {
            "status": "success",
            "data": serializer.data
        }     
        return Response(data, status=status.HTTP_200_OK)


class userdata(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    








