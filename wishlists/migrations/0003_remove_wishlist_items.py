# Generated by Django 3.1.3 on 2020-12-02 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0002_auto_20201201_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='items',
        ),
    ]
