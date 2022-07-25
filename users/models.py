from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models

import uuid

from users.utils import CustomUserManager

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
  
    canvases = models.ForeignKey(
    "canvases.Canvas", on_delete=models.CASCADE, related_name="users", null=True
  )
  

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
