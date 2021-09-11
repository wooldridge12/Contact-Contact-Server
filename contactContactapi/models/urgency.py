from django.db import models


class Urgency(models.Model):
    """Urgency Model"""
    label = models.CharField(max_length=50)
