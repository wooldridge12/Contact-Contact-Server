from django.db import models


class Message(models.Model):
    """Message Model"""
    sender = models.ForeignKey("ContactUser", on_delete=models.CASCADE, related_name="mesages")

    reciever = models.ForeignKey("ContactUser", on_delete=models.CASCADE)

    help_section_post = models.ForeignKey("HelpSectionPost", on_delete=models.CASCADE)

    message = models.CharField(max_length=300)

    created_on_date = models.IntegerField()
