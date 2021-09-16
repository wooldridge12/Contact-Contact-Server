"""View module for handling requests about battle buddies"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from contactContactapi.models import BattleBuddy, ContactUser


class BattleBuddyView(ViewSet):
    """ContactContact Battle Buddy"""

    def list(self, request):

        battle_buddies = BattleBuddy.objects.all()

        serializer = BattleBuddySerializer(
            battle_buddies, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def create(self, request):

        contact_user = ContactUser.objects.get(user=request.auth.user)

        battle_buddy = BattleBuddy()
        battle_buddy.active = request.data["active"]
        battle_buddy.contact_user = contact_user

        try:
            battle_buddy.save()
            serializer = BattleBuddySerializer(battle_buddy, context={'request': request})
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

class BattleBuddySerializer(serializers.ModelSerializer):
    """"""
    contact_user = ContactUserSerializer(many=False)

    class Meta:
        model = BattleBuddy
        fields = ['contact_user', 'active']