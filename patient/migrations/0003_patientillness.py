# Generated by Django 4.2 on 2024-10-02 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_medicinecontainer"),
        ("patient", "0002_patienttreatment_patienthistory"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientIllness",
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
                    "illness_gravity",
                    models.CharField(
                        blank=True,
                        choices=[("I", "estadio 1"), ("II", "estadio 2")],
                        null=True,
                    ),
                ),
                ("notes", models.TextField(blank=True, null=True)),
                ("treatment", models.TextField(blank=True, null=True)),
                (
                    "illness",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.illness",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patient.patient",
                    ),
                ),
            ],
            options={
                "db_table": "patient_illness",
            },
        ),
    ]
