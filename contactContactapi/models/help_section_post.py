from django.db import models


class HelpSectionPost(models.Model):
    """HelpSectionPost Model"""
    contact_user = models.ForeignKey("ContactUser", on_delete=models.CASCADE)

    urg_button = models.ForeignKey("Urgency", on_delete=models.CASCADE)

    content = models.CharField(max_length=500)

    phone_number = models.IntegerField()

    is_helped = models.BooleanField(default=False)
