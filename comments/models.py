from django.db import models
from accounts.models import User


class Comment(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=360)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
