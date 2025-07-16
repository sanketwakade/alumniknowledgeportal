from django.db import models

class Knowledge(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    graduation_year = models.CharField(max_length=10)
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
