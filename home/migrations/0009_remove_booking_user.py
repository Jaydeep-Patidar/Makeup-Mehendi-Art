# Generated by Django 5.1.3 on 2024-12-20 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_booking_status_booking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
