# Generated by Django 5.0.6 on 2024-07-10 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_remove_repository_resources_repository_resource"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="parent_resource",
            field=models.ForeignKey(
                db_column="parent_resource_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app.resource",
            ),
        ),
    ]
