# Generated by Django 4.2 on 2024-09-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="document",
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
