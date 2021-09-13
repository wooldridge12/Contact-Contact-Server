"""View module for handling requests about urgency"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from contactContactapi.models import Urgency

class UrgencyView(ViewSet):
    """ContactContact Urgency"""

    def list(self, request):
        urgency = Urgency.objects.all()

        serializer = UrgencySerializer(
            urgency, many=True, context={'request': request}
        )
        return Response(serializer.data)



class UrgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Urgency
        fields = ('id', 'label')
        depth = 1
        