# Generated by Django 4.2.7 on 2023-11-24 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_bookings_journey_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='Cust_Accept_Status',
        ),
    ]