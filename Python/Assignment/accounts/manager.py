from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and returns a regular user with the given username and password.
        """
        if not username:
            raise ValueError("The username field must be set")
        
        # Normalize the username (ensures consistency)
        username = self.model.normalize_username(username)
        
        # Set default fields or accept extra fields
        extra_fields.setdefault('is_active', True)  # Ensure user is active by default
        
        # Create the user
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save to the database
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and returns a superuser with the given username and password.
        """
        # Ensure superuser fields are properly set
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(username, password, **extra_fields)
