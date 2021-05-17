from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=255)
    contact_message = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)