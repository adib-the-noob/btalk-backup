# Generated by Django 4.2.1 on 2023-07-03 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_alter_friendrequest_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]
