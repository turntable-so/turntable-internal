# Generated by Django 5.0.6 on 2024-07-09 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_column_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="column",
            name="type",
            field=models.TextField(),
        ),
    ]
