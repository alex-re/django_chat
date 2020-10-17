from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def last_10_messages():
        # return Message.objects.order_by('-timestamp').all()[:10]
        return Message.objects.order_by('timestamp').all()[:10]
    
    def __str__(self):
        return f'from {self.author.username}'
