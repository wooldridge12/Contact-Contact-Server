from django.db import models


class Post(models.Model):
    """Post Model"""
    contact_user = models.ForeignKey("ContactUser", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    