from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=64)

    def __str__(self):
        return self.username
