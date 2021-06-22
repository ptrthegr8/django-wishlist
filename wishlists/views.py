from django.shortcuts import render, get_object_or_404, redirect
from wishlists.models import Wishlist
from wishlists.forms import AddWishlistForm


def index_view(reqeust):
    wishlists = Wishlist.objects.all()
    return render(reqeust, "index.html", {"wishlists": wishlists})


def list_detail_view(request, id):
    html = "list_detail.html"
    wishlist = get_object_or_404(Wishlist, id=id)
    context = {"wishlist": wishlist}
    return render(request, html, context)


def add_wishlist_view(request):
    html = "generic_form.html"
    form = AddWishlistForm()
    if request.method == "POST":
        form = AddWishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.creator = request.user
            wishlist.save()
            return redirect(f"/list/{wishlist.id}/")
    return render(request, html, {"form": form})
