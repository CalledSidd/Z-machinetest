# Generated by Django 4.1.6 on 2023-02-14 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parser", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="miles_per_gallon",
            field=models.FloatField(default=0),
        ),
    ]
