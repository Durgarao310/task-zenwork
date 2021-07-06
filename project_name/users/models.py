from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email        = models.EmailField(unique=True)
    phone_number = models.CharField(blank=True, null=True, max_length=15)
    address      = models.TextField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email