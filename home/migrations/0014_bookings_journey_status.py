# Generated by Django 4.1.7 on 2023-10-31 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_bookings_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='Journey_Status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='', max_length=50),
        ),
    ]
