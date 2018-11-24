from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Room(models.Model):
    creator = models.ForeignKey(User, on_delete         = models.CASCADE)
    invited = models.ManyToManyField(User, related_name = "invited_users")
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Chat room'
        verbose_name_plural = 'Chat rooms'

class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField(max_length=100)
    date = models.DateTimeField(default = timezone.now)

    class Meta:
        verbose_name = 'Chat message'
        verbose_name_plural = 'Chat messagess'

