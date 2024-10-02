# Generated by Django 4.2 on 2024-10-02 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0004_alter_patientillness_patient"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patienthistory",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="histories",
                to="patient.patient",
            ),
        ),
        migrations.AlterField(
            model_name="patienttreatment",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="treatments",
                to="patient.patient",
            ),
        ),
    ]
