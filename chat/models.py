from django.db import models
from django.contrib import admin

# Create your models here.

class ChatMessage(models.Model):
    sender = models.CharField(max_length=10)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100)


admin.site.register(ChatMessage)
