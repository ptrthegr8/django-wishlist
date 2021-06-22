from django import forms
from list_items.models import ListItem


class AddListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ("title", "url", "parent")
