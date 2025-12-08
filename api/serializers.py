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