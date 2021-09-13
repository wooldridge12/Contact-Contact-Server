"""View module for handling requests about helpsectionposts"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from contactContactapi.models import HelpSectionPost, ContactUser, Urgency

class HelpSectionPostView(ViewSet):
    """ContactContact HelpSectionPost"""

    def list(self, request):

        help_section_posts = HelpSectionPost.objects.all()

        serializer = HelpSectionPostSerializer(
            help_section_posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def create(self, request):

        contact_user = ContactUser.objects.get(user=request.auth.user)
        urg_button = Urgency.objects.get(pk=request.data["urg_button"])

        helpsectionpost = HelpSectionPost()
        helpsectionpost.contact_user = contact_user
        helpsectionpost.urg_button = urg_button
        helpsectionpost.content = request.data["content"]
        helpsectionpost.phone_number = request.data["phone_number"]
        helpsectionpost.is_helped = request.data["is_helped"]

        try:
            helpsectionpost.save()
            serializer = HelpSectionPostSerializer(helpsectionpost, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


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


class HelpSectionPostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializer type
    """
    contact_user = ContactUserSerializer(many=False)

    class Meta:
        """"""
        model = HelpSectionPost
        fields = ('id', 'content','contact_user', 'urg_button', 'phone_number', 'is_helped' )
        depth = 1
        