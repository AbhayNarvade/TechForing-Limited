from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']  # Only return the user-specified fields
        

    def create(self, validated_data):
        """
        Override create method to hash the password before saving the user instance
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Override update method to handle password update if it's provided
        """
        password = validated_data.pop('password', None)  # Pop the password if it's present

        # Update other fields
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)  # Hash the password
            instance.save()
       

        return instance