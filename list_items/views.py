from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from list_items.models import ListItem
from list_items.forms import AddListItemForm


def item_detail_view(request, id):
    html = "item_detail.html"
    item = get_object_or_404(ListItem, id=id)
    context = {"item": item}
    return render(request, html, context)


@login_required
def claim_item_view(request, id):
    item = get_object_or_404(ListItem, id=id)
    item.claimed_by = request.user
    item.save()
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def add_item_view(request):
    html = "generic_form.html"
    form = AddListItemForm()
    if request.method == "POST":
        form = AddListItemForm(request.POST)
        if form.is_valid():
            list_item = form.save(commit=False)
            # list_item.title
            # list_item.url
            # list_item.parent
            # list_item.claimed_by
            list_item.save()
            return redirect(f"/list/{list_item.parent.id}/")
    return render(request, html, {"form": form})