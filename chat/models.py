from django.db import models
from django.contrib import admin

# Create your models here.

class ChatMessage(models.Model):
    sender = models.CharField(max_length=10)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.CharField(max_length=100)


class ChatSession(models.Model):
    session_id = models.CharField(max_length=100, unique=True)
    is_human = models.BooleanField(default=False)
    order_history = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


admin.site.register(ChatMessage)
admin.site.register(ChatSession)
