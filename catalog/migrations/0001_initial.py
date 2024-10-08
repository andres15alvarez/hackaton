# Generated by Django 4.2 on 2024-09-27 21:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FrequentQuestion",
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
                ("question", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=100)),
                ("is_visible", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "frequent_question",
            },
        ),
        migrations.CreateModel(
            name="Illness",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "illness",
            },
        ),
        migrations.CreateModel(
            name="Medicine",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "medicine",
            },
        ),
        migrations.CreateModel(
            name="Sector",
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
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "sector",
            },
        ),
        migrations.CreateModel(
            name="IllnessMedicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "illness",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.illness",
                    ),
                ),
                (
                    "medicine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.medicine",
                    ),
                ),
            ],
            options={
                "db_table": "illness_medicine",
            },
        ),
    ]
