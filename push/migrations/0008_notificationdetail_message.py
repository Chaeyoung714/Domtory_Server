# Generated by Django 4.2.7 on 2024-07-13 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0007_notificationdetail_lost_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationdetail',
            name='message',
            field=models.BooleanField(default=True),
        ),
    ]
