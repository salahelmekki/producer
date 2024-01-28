from django.db import models


class Message(models.Model):
    """
    Model representing a message to be sent to the consumer.
    """
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
