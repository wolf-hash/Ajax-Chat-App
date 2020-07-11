from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, primary_key=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    ipaddress = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.ForeignKey(Room, on_delete=models.CASCADE)
    messages = models.TextField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True, null=True)
    ipaddress = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.messages