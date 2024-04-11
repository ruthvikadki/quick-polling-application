from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)

    def __str__(self):
        return self.username
