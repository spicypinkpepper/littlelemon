# Generated by Django 4.2.6 on 2023-10-23 15:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_booking_no_of_guests_menu_inventory'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='No_of_guests',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='menu',
            name='Inventory',
            field=models.IntegerField(default=1),
        ),
    ]
