# Generated by Django 4.1.6 on 2023-02-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("supers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="super",
            name="super_type",
            field=models.CharField(
                choices=[("Hero", "Hero"), ("Villain", "Villain")], max_length=7
            ),
        ),
    ]
