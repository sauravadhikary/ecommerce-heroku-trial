# Generated by Django 3.0.8 on 2020-07-08 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_remove_auctionlisting_disc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='description',
            new_name='discription',
        ),
    ]
