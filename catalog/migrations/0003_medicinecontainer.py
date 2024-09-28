# Generated by Django 4.2 on 2024-09-28 02:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_medicine_illnesses"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicineContainer",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Register created timestamp"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="Last update timestampt"
                    ),
                ),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
                ("grammage", models.FloatField()),
                ("code", models.CharField(max_length=10)),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.medicine",
                    ),
                ),
            ],
            options={
                "db_table": "medicine_container",
            },
        ),
    ]
