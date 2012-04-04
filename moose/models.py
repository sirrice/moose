from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):
    sender = models.ForeignKey(User, related_name='feedback_sender')
    receiver = models.ForeignKey(User, related_name='feedback_receiver')

class Message(models.Model):
    thread = models.ForeignKey(Feedback)
    text = models.TextField()
    date = models.DateTimeField()
    from_sender = models.BooleanField()
