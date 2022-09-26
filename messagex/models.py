from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import secured_fields

# Create your models here.

class Messagex(models.Model):
    sender = models.ForeignKey(
        User, 
        models.SET_NULL,
        verbose_name="Sender:",
        related_name="sender",
        blank=True,
        null=True,
        )
    recipient = models.ForeignKey(
        User, 
        models.SET_NULL,
        verbose_name="Recipient:",
        related_name="recipient",
        blank=False,
        null=True,
        )
    subject = secured_fields.EncryptedCharField(max_length=256, default="", verbose_name="Subject:")
    text = secured_fields.EncryptedCharField(max_length=256, default="", verbose_name="Message:")
    time_stamp = secured_fields.EncryptedDateTimeField(default=now, verbose_name="Timestamp:")

    
    def __str__(self):
        return self.subject + " " + self.text + " " + str(self.time_stamp) + " " + str(self.sender) + " " + str(self.recipient)

    def get_absolute_url(self):
        return "/messagex/sent"