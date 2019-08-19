from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student      = models.BooleanField(default=False)
    is_instructor   = models.BooleanField(default=False)
    is_coordinator  = models.BooleanField(default=False)
