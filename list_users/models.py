from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ListUser(AbstractUser):
    friends = models.ManyToManyField("self", symmetrical=True)