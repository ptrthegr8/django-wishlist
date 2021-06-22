from django import forms
from wishlists.models import Wishlist

class AddWishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ["title"]
