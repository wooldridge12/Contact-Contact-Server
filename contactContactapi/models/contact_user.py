from django.db import models
from django.contrib.auth.models import User


class ContactUser(models.Model):
    "ContactUser Model"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)