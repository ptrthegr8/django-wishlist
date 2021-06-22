from django.db import models
from django.utils import timezone
from list_users.models import ListUser


class Wishlist(models.Model):
    title = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(ListUser, models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
