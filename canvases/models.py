from django.db import models
import uuid

class Canvas(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    reference = models.TextField()
    