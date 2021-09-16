"""View module for handling requests about messages"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from contactContactapi.models import Message, BattleBuddy, ContactUser, HelpSectionPost


class MessageView(ViewSet):
    """ContactContact Message"""

    def list(self, request):

        messages = Message.objects.filter(sender__user = request.auth.user)

        serializer = MessageSerializer(
            messages, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            message = Message.objects.get(pk=pk)
            serializer = MessageSerializer(message, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):

        contact_user = ContactUser.objects.get(user=request.auth.user)
        battle_buddy = ContactUser.objects.get(pk=request.data["battle_buddy"])
        help_section_post = HelpSectionPost.objects.get(pk=request.data["help_section_post"])

        message = Message()
        message.sender = contact_user
        message.reciever = battle_buddy
        message.help_section_post = help_section_post
        message.message = request.data["message"]
        message.created_on_date = request.data["created_on_date"]

        try:
            message.save()
            serializer = MessageSerializer(message, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users name"""
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ContactUserSerializer(serializers.ModelSerializer):
    """"""
    user = UserSerializer(many=False)

    class Meta:
        model = ContactUser
        fields = ['user']

class MessageSerializer(serializers.ModelSerializer):
    """JSON serializer for posts

    Arguments:
        serializer type
    """

    class Meta:
        """"""
        model = Message
        fields = ('id', 'sender', 'reciever', 'message', 'help_section_post', 'created_on_date' )
        depth = 2
        