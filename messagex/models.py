from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import secured_fields

# Create your models here.

class Messagex(models.Model):
    UNREAD = 'UR'
    READ = 'RD'
    MODIFIED = 'MD'
    DELETED = 'DL'
    MESSAGE_STATUS = [
        (UNREAD, 'Unread'),
        (READ, 'Read'),
        (MODIFIED, 'Modified'),
        (DELETED, 'Deleted')
    ]
    subject = models.CharField(max_length=50, default="", verbose_name="Message Subject")
    text = models.CharField(max_length=256, default="", verbose_name="Message Text")
    etext = secured_fields.EncryptedCharField(max_length=256, default="", verbose_name="Encrypted Message Text")
    status = models.CharField(max_length=2, choices=MESSAGE_STATUS, default="UR", verbose_name="Message Status")
    timestamp = models.DateTimeField(default=now, verbose_name="Message Timestamp")
    sender = models.ForeignKey(
        User, 
        models.SET_NULL,
        verbose_name="Message Sender",
        related_name="sender",
        blank=True,
        null=True,
        )
    recipient = models.ForeignKey(
        User, 
        models.SET_NULL,
        verbose_name="Message Recipient",
        related_name="recipient",
        blank=True,
        null=True,
        )
    
    def __str__(self):
        return self.text + " " + str(self.etext) + " " + self.status + " " + str(self.timestamp) + " " + str(self.sender) + " " + str(self.recipient)

    def get_absolute_url(self):
        return "/messagex/list"