from django.contrib.auth.models import User
from django.db import models

import re

#receiver is person who asked question
#sender is person sending feedback
#reword and refactor them :)

SHORTNAME_PATTERN = "^[a-z\-\_1-9]+"
SHORTNAME_REGEX = re.compile(SHORTNAME_PATTERN)
class Question(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=128)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    shortname = models.CharField(max_length=100, blank=False, null=False)

SENDER_STATUSES = (
    (u'anon', u'Anonymous'),
    (u'email', u'Email Only'),
    (u'user', u'Linked to User'),
)

class Sender(models.Model):
    user = models.ForeignKey(User, null=True)
    email = models.EmailField(null=True)
    status = models.CharField(max_length=6, choices=SENDER_STATUSES)

class Feedback(models.Model):
    sender = models.ForeignKey(Sender)
    question = models.ForeignKey(Question)

class Message(models.Model):
    feedback = models.ForeignKey(Feedback)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    from_sender = models.BooleanField()
