# Generated by Django 4.2.1 on 2023-07-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_remove_messageattachment_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageattachment',
            name='file_name',
            field=models.CharField(default='attachment', max_length=255),
        ),
    ]
