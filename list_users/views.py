from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, reverse, get_object_or_404

from list_users.models import ListUser
from wishlists.models import Wishlist

from .forms import LoginForm, SignupForm


def signup_view(request):
    template = "generic_form.html"
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            list_user = ListUser.objects.create_user(
                username=data["username"],
                email=data["email"],
                password=data["password"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )

            if list_user:
                login(request, list_user)
                return redirect(request.GET.get("next", "/"))
    return render(request, template, {"form": form})


def login_view(request):
    template = "generic_form.html"
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            list_user = authenticate(
                request, username=data["username"], password=data["password"]
            )

            if list_user:
                login(request, list_user)
                return redirect(request.GET.get("next", "/"))
    return render(request, template, {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/login/")


def user_detail_view(request, id):
    html = "user_detail.html"
    list_user = get_object_or_404(ListUser, id=id)
    wishlists = Wishlist.objects.filter(creator=list_user)
    context = {"wishlists": wishlists}
    if request.user.id == list_user.id:
        claimed_items = list_user.claimed.all()
        context.update({"claimed_items": claimed_items})
    return render(request, html, context)
