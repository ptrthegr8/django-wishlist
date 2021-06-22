# Generated by Django 3.1.3 on 2020-12-02 15:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listuser',
            name='friends',
            field=models.ManyToManyField(related_name='_listuser_friends_+', to=settings.AUTH_USER_MODEL),
        ),
    ]