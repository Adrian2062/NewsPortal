from tokenize import Comment
from django.contrib.auth.models import Group, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups", "first_name", "last_name"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id","content", "created_at", "post", "user"]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'user': {'read_only': True},
            'post': {'read_only': True},
        }

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True,min_length=8)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "A user with that email already exists."
                )
        return value
    
    def create(self, validated_data):
        email = validated_data.get("email", "")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=email,
            password=validated_data["password"],
        )
        return user