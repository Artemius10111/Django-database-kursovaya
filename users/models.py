from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, auto_created=True)
    def __str__(self) -> str:
        return self.username
