from django.db import models


class Message(models.Model):
    """Message Model"""
    contact_user = models.ForeignKey("ContactUser", on_delete=models.CASCADE)

    battle_buddy = models.ForeignKey("BattleBuddy", on_delete=models.CASCADE)

    help_section_post = models.ForeignKey("HelpSectionPost", on_delete=models.CASCADE)

    message = models.CharField(max_length=300)

    created_on_date = models.IntegerField()
