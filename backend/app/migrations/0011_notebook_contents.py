# Generated by Django 5.0.6 on 2024-07-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_alter_asset_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="notebook",
            name="contents",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
