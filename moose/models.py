from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField( auto_now_add=True)
#    shortname = models.CharField(max_length=100, blank=False, null=False)

# class Feedback(models.Model):
    
#     receiver = models.ForeignKey(User, related_name='feedback_receiver')

class Feedback(models.Model):
    sender = models.ForeignKey(User, null=True)
    sender_name = models.CharField(max_length=128)
    question = models.ForeignKey(Question)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    from_sender = models.BooleanField()
