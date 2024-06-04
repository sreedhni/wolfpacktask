from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password2 = serializers.CharField(write_only=True, required=True, help_text="Enter password again for confirmation.")

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2']
        extra_kwargs = {
            'password': {'min_length': 8, 'help_text': 'Password must be at least 8 characters long.'},
        }

    def create(self, validated_data):
        """
        Create a new user instance with the provided validated data.
        
        Args:
            validated_data (dict): Validated data for user creation.
        
        Returns:
            User: The created user instance.
        
        Raises:
            serializers.ValidationError: If the passwords do not match.
        """
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        user = User.objects.create_user(**validated_data, password=password)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    """
    Serializer for user login.
    """
    email = serializers.EmailField(required=True, help_text="Enter your email address.")
    password = serializers.CharField(required=True, help_text="Enter your password.")

    class Meta:
        model = User
        fields = ['email', 'password']
