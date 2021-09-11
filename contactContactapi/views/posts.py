"""View module for handling requests about posts"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from contactContactapi.models import Post, ContactUser

class PostView(ViewSet):
    """ContactContact Post"""

    def list(self, request):

        posts = Post.objects.all()

        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users name"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ContactUserSerializer(serializers.ModelSerializer):
    """HI"""
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
        """HI"""
        model = Post
        fields = ('id', 'content','contact_user')
        depth = 1
        