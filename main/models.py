from django.db import models
from django.contrib.auth.models import User

# Create your models here.
roles = [
        ('admin', 'Admin'),
        ('user', 'User'),
        ('guest', 'Guest'),
    ]


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=roles, default='guest')

