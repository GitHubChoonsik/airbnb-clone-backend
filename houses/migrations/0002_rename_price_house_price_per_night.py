# Generated by Django 4.2.7 on 2023-11-28 15:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("houses", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="house",
            old_name="price",
            new_name="price_per_night",
        ),
    ]
