from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import AuctionListing, Bid, Comment, User


def index(request):
    return render(request, "auctions/index.html", {
        "listings": AuctionListing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def listings(request, listid):
    list = AuctionListing.objects.get(pk=listid)
    if request.method == "POST":
        comment = request.POST["comment"]
        cmt = Comment(listing= list, mycomment=comment, comment_by= request.user)
        cmt.save()
    else:
        pass    
    return render(request, "auctions/listing.html", {
        "listing": list,
    })

def bid(request, listid):
    list = AuctionListing.objects.get(pk=listid)
    if request.method == "POST":
        bidrate = int(request.POST["bidvalue"])
        higestbid = list.startingbid
        if bidrate > higestbid:
            newBid = Bid(listing=list, bid_by=request.user, mybid=bidrate )
            newBid.save()
            list.startingbid = bidrate
            list.save()
            return render(request, "auctions/listing.html", {
                "listing": list,
            })
        else:
            return HttpResponse("Error: Bid Not Enough")
    else:
        pass
            

