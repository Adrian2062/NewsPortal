from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView

from api.serializers import CommentSerializer, GroupSerializer, UserRegistrationSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentListcreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
    def get(self, request, post_id, *args, **kwargs):
        comments = Comment.objects.filter(post=post_id).order_by("-created_at")
        serialized_data = CommentSerializer(comments, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def post(self, request, post_id, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailAPIView(APIView):
    permission_classes = [IsStaffOrOwner] 

    def get_object(self, pk):
        try:
            obj = Comment.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except Comment.DoesNotExist:
            raise exceptions.NotFound({"detail": "Comment not found."}) 


    def get(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serialized_data = CommentSerializer(comment).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def put(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, partial=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def patch(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, post_id, pk, *args, **kwargs):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]