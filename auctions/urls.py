from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("mylisting", views.mylisting, name="mylisting"),
    path("mybids", views.mybids, name="mybids"),
    path("listingview/<int:listid>", views.listings, name="listingview"),
    path("bid/<int:listid>", views.bid, name="bid"),
]
