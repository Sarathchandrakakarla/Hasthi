# Generated by Django 4.1.7 on 2023-09-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='Pay_Status',
            field=models.IntegerField(default=0),
        ),
    ]
