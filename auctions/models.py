from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

category_choices = (
    ("fashion","Fashion"),
    ("toys", "Toys"),
    ("electronics", "Electronics"),
    ("home", "Home Appliences"),
    ("stationary", "Stationary Objects"),
    ("computer", "Computer and Pheripherals"),
    ("nocategory", "No Category Selected"),
)

class AuctionListing(models.Model):
    created_by = models.ForeignKey(User, on_delete= models.PROTECT, related_name="mylistings")
    title = models.CharField(max_length=64)
    discription = models.TextField()
    startingbid = models.IntegerField()
    imageurl = models.URLField(max_length=256)
    category = models.CharField(max_length=15, choices=category_choices, default="nocategory")
    timestamp = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return f"{self.pk}: {self.title} -- {self.created_by}"
    


class Bid(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete= models.PROTECT, related_name="sourcelisting", null=True)
    bid_by = models.ForeignKey(User, on_delete= models.PROTECT, related_name="allbids", null=True)
    mybid = models.IntegerField( null=True)
    timestamp = models.DateTimeField(auto_now_add=True , null=True)
    # timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.bid_by} bids $ {self.mybid} "


class Comment(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete= models.PROTECT, related_name="commentedlisting", null=True)
    comment_by = models.ForeignKey(User, on_delete= models.PROTECT, related_name="allcomments", null=True)
    mycomment = models.TextField( null=True)
    timestamp = models.DateTimeField(auto_now_add=True , null=True)