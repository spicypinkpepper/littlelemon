# Generated by Django 4.2.6 on 2023-10-23 15:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_booking_no_of_guests_remove_menu_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AddField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
