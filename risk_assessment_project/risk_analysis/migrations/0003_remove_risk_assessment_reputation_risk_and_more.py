# Generated by Django 5.1.6 on 2025-02-20 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("risk_analysis", "0002_risk_assessment_cybersecurity_risk_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="risk_assessment",
            name="reputation_risk",
        ),
        migrations.RemoveField(
            model_name="risk_assessment",
            name="supply_chain_risk",
        ),
        migrations.AddField(
            model_name="risk_assessment",
            name="employees",
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name="risk_assessment",
            name="location",
            field=models.CharField(default="unknown", max_length=255),
        ),
        migrations.AddField(
            model_name="risk_assessment",
            name="revenue",
            field=models.PositiveIntegerField(default=10),
        ),
    ]
