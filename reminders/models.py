from django.db import models
from authentication.models import CustomUser


class Reminder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    reminder_type = models.CharField(max_length=20)  # SMS, Email, etc.
