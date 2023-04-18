from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
