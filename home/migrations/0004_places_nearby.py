# Generated by Django 4.1.7 on 2023-09-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_places'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='Nearby',
            field=models.TextField(null=True),
        ),
    ]
