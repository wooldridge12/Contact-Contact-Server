from django.db import models


class BattleBuddy(models.Model):
    """BattleBuddy Model"""
    contact_user = models.ForeignKey("ContactUser", on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    