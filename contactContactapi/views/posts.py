"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from contactContactapi.models import Post, ContactUser, Urgency

class PostView(ViewSet):
    """ContactContact Post"""

    def list(self, request):

        posts = Post.objects.all()

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):

        contact_user = ContactUser.objects.get(user=request.auth.user)

        post = Post()
        post.content = request.data["content"]
        post.contact_user = contact_user


        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Destroy"""
        try:
            post = Post.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users name"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ContactUserSerializer(serializers.ModelSerializer):
    """"""
    user = UserSerializer(many=False)

    class Meta:
        model = ContactUser
        fields = ['user']


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializer type
    """
    contact_user = ContactUserSerializer(many=False)

    class Meta:
        """"""
        model = Post
        fields = ('id', 'content','contact_user')
        depth = 1
        