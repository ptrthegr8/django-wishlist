from django.db import models
from list_users.models import ListUser
from wishlists.models import Wishlist

# Create your models here.
class ListItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    parent = models.ForeignKey(Wishlist, models.CASCADE, related_name="listitems")
    claimed_by = models.ForeignKey(
        ListUser, models.CASCADE, related_name="claimed", null=True, blank=True
    )

    def __str__(self):
        return self.title
